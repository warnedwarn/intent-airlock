# Readiness matrix

| Gate | Required proof | Status |
|---|---|---|
| Semantic necessity | Closed category and risk classification against a fetched policy | PASS source/tests |
| Cumulative consequence | An authorized result consumes exactly one deterministic quota unit | PASS source/tests |
| Cross-wallet replay | Normalized intent fingerprint checked before consensus and mutation | PASS source/tests/live |
| Consensus integrity | Validators bind policy digest, category, integer risk, and reason code | PASS source/tests |
| Authorization | Only the submitting wallet can consume one cleared action | PASS source/tests |
| Deployment/source match | Finalized StudioNet deployment equals repository contract bytes | PASS |
| Live lifecycle | Open, request, consume, replay rejection, before/after readback | PASS (`AIRLOCK-1791581900`) |
| Public browser | Canonical Cloudflare build uses deployed address and complete workflow | PASS desktop/mobile (`evidence/browser-verification.json`) |
