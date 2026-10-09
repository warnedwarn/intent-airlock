# INTENT AIRLOCK

`SEMANTIC RATE CONTROL / STUDIONET`

Autonomous systems often receive permissions one action at a time while the real risk is cumulative. Ten individually acceptable exports can still exhaust a disclosure budget. Intent Airlock makes that missing state visible.

## Flight rule

An operator opens one airlock around a public HTTPS policy, a closed category vocabulary, a quota for each category, and a maximum risk level. Validators retrieve the complete policy, bind its SHA-256 digest, and agree on the exact category, integer risk, and reason code for every proposed action.

The model never spends capacity. Contract code checks the agreed result against the frozen threshold and current counter. An authorized action increments exactly one quota; a blocked action increments nothing. The submitter may consume its own clearance once.

Normalized action text is fingerprinted before consensus. Replaying an earlier intent from a different wallet cannot burn another unit of capacity or trigger another model call.

## Instrument panel

The interface is a control room rather than an exposed method form. A sweep radar shows pending intent, circular instruments show cumulative category use, and each finalized classification becomes a flight strip. The mission drawer keeps policy and action inputs subordinate to the live state.

## Commands

```text
python -m pytest -q
genvm-lint contracts/contract.py
python scripts/deploy.py
python scripts/smoke.py
python scripts/verify_deployment.py
```

## Fixture boundary

The repository policy and demo wallets are operator-controlled fixtures. They prove policy-digest binding, exact semantic classification, cumulative quota mutation, submitter-only execution, and cross-wallet replay rejection. They are not independent organizations.

Deployment and live transaction evidence are recorded after StudioNet verification in `deployment.json` and `evidence/`.
