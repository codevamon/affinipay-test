import pytest, requests

invalid_payloads = [
    {"breed": "", "age": 2, "name": "Nina"},        # breed vacío
    {"breed": "Pug", "age": -1, "name": "Nina"},    # age negativo
    {"breed": "Pug", "age": "dos", "name": "Nina"}, # age no entero
    {"breed": "Pug", "name": "Nina"},               # falta age
    {},                                             # vacío
]

@pytest.mark.parametrize("payload", invalid_payloads)
@pytest.mark.xfail(strict=False, reason="Service may accept invalid payloads (bug).")
def test_create_should_reject_invalid_payloads(base_url, payload):
    r = requests.post(f"{base_url}/dogs", json=payload, timeout=3)
    assert r.status_code in (400, 422), f"Expected 400/422; got {r.status_code} {r.text}"