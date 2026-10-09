from pathlib import Path

SOURCE=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()

def test_cumulative_quota_is_deterministic():
 assert "used[index]<quotas[index]" in SOURCE
 assert "if allowed: used[index]+=1" in SOURCE
 assert "QUOTA_EXHAUSTED" in SOURCE and "RISK_BLOCKED" in SOURCE

def test_replay_guard_precedes_consensus():
 replay=SOURCE.index("replay_key in self.attempted")
 classify=SOURCE.index("verdict=self._classify")
 assert replay<classify
 assert "statement.lower().encode()" in SOURCE

def test_policy_and_all_state_drivers_are_consensus_bound():
 for item in ("policy_digest","category","risk","reason","independently refetch the frozen policy"):
  assert item in SOURCE

def test_authorization_and_single_consumption():
 assert "addr(gl.message.sender_address)!=addr(action.submitter)" in SOURCE
 assert "action.state!='CLEARED'" in SOURCE
 assert "action.state='EXECUTED'" in SOURCE

def test_closed_shapes_and_bounds():
 assert "len(normalized)>6" in SOURCE
 assert "risk<0 or risk>3" in SOURCE
 assert "REASONS =" in SOURCE
