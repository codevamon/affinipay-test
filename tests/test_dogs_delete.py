import requests

def test_delete_then_get_is_404(base_url, dog_factory):
    did, _ = dog_factory(name="ToDelete")
    r = requests.delete(f"{base_url}/dogs/{did}", timeout=3)
    assert r.status_code in (200, 204), f"DELETE /dogs/{did} => {r.status_code} {r.text}"

    r2 = requests.get(f"{base_url}/dogs/{did}", timeout=3)
    # Algunas APIs devuelven 404; algunas 410; documenta si no es así
    assert r2.status_code in (404, 410), f"GET after delete should be 404/410; got {r2.status_code}"
