import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

def calldata_compat(method=None,args=None,kwargs=None):
 out={}
 if method is not None: out['method']=method
 if args: out['args']=args
 if kwargs: out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=calldata_compat

ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text(); DEPLOY=json.loads((ROOT/'deployment.json').read_text()); ADDRESS=DEPLOY['contractAddress']
def account(number): return create_account(account_private_key=re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip())
def client(acct): return create_client(chain=studionet,account=acct)
def wait(c,tx,expect='SUCCESS'):
 receipt=c.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True); leaders=receipt.get('consensus_data',{}).get('leader_receipt')or[]; leaders=[leaders] if isinstance(leaders,dict) else leaders; executions=[str(row.get('execution_result','')).upper() for row in leaders]; assert receipt.get('result_name')=='MAJORITY_AGREE' and expect in executions; return receipt,executions
def write(c,name,args,expect='SUCCESS'):
 tx=c.write_contract(address=ADDRESS,function_name=name,args=args); print(name+'_tx='+str(tx),flush=True); _,executions=wait(c,tx,expect); return str(tx),executions

owner=account(2); operator=create_account(); replay=create_account(); oc=client(owner); pc=client(operator); rc=client(replay); stamp=str(int(time.time())); aid='AIRLOCK-'+stamp; xid='READ-'+stamp; policy='https://raw.githubusercontent.com/warnedwarn/intent-airlock/main/docs/evidence/flight-policy.md'; description='Read the archive index and compare record titles without changing stored data.'; tx={}
tx['open'],_=write(oc,'open_airlock',[aid,'Archive action perimeter',policy,['READ','WRITE','ADMIN'],[3,2,1],1]); tx['request'],_=write(pc,'request_clearance',[aid,xid,description]); tx['consume'],_=write(pc,'consume_clearance',[xid]); before=oc.read_contract(address=ADDRESS,function_name='get_airlock',args=[aid]); action=oc.read_contract(address=ADDRESS,function_name='get_action',args=[xid]); assert before['used']==[1,0,0] and action['state']=='EXECUTED' and action['decision']=='AUTHORIZED'
replay_tx=rc.write_contract(address=ADDRESS,function_name='request_clearance',args=[aid,'REPLAY-'+stamp,'  read the archive index and compare record titles without changing stored data.  ']); tx['replay']=str(replay_tx); replay_receipt,replay_execution=wait(rc,replay_tx,'ERROR'); after=oc.read_contract(address=ADDRESS,function_name='get_airlock',args=[aid]); assert after['used']==before['used']==[1,0,0] and after['action_ids']==before['action_ids']==[xid]
proof={'airlockId':aid,'actionId':xid,'contract':ADDRESS,'transactions':tx,'positive':{'category':action['category'],'risk':action['risk'],'decision':action['decision'],'state':action['state'],'used':before['used']},'normalizedReplay':{'consensus':replay_receipt.get('result_name'),'execution':replay_execution,'usedBefore':before['used'],'usedAfter':after['used'],'actionsBefore':before['action_ids'],'actionsAfter':after['action_ids']},'fixtureDisclosure':'The policy page and wallets are operator-controlled fixtures used to prove cumulative quota and cross-wallet replay behavior.'}; (ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n'); print(json.dumps(proof,indent=2),flush=True)
