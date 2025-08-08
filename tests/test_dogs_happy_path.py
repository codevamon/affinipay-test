import requests

def test_list_endpoint_up(base_url, norm):
    r = requests.get(f"{base_url}/dogs/", timeout=3)
    assert r.status_code == 200
    data = norm(r.json())
    assert isinstance(data, list), f"Expected list; got {type(data).__name__}: {data}"

def test_create_and_get_by_id(base_url, dog_factory):
    did, created = dog_factory(breed="Beagle", age=2, name="Luna")

    # GET detalle
    r = requests.get(f"{base_url}/dogs/{did}", timeout=3)
    assert r.status_code == 200, f"GET /dogs/{did} => {r.status_code} {r.text}"
    data = r.json()

    # Campos básicos
    assert str(data.get("id")) == str(did)
    assert data.get("breed") in ("Beagle", created.get("breed"))
    assert int(data.get("age")) == int(created.get("age", 2))
    assert data.get("name") in ("Luna", created.get("name"))