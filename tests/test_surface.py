from pathlib import Path

HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text()

def test_control_room_has_complete_flow():
 for item in ('OPEN AIRLOCK','REQUEST CLEARANCE','CONSUME','SEAL EPOCH','FINALIZED','open_airlock','request_clearance','consume_clearance','get_airlock'):
  assert item in HTML

def test_visual_identity_is_not_a_generic_form_grid():
 for item in ('radar','flight-strip','quota-ring','telemetry'):
  assert item in HTML
 assert 'card-grid' not in HTML and '<pre' not in HTML
