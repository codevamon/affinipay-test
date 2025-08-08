import os, time, pytest, requests

BASE_URL = os.getenv("DOGS_BASE_URL", "http://127.0.0.1:5000")

def _healthcheck(url):
    # Intenta /dogs y /dogs/ por si hay redirect de slash
    for path in ("/dogs", "/dogs/"):
        try:
            r = requests.get(url + path, allow_redirects=True, timeout=2)
            if r.status_code == 200:
                return True
        except Exception:
            pass
    return False

@pytest.fixture(scope="session")
def base_url():
    # Espera hasta 9s a que el contenedor levante
    for _ in range(30):
        if _healthcheck(BASE_URL):
            break
        time.sleep(0.3)
    return BASE_URL

def _normalize_list_response(resp_json):
    """
    Algunos builds devuelven {} en vez de [] para colecciones vacías.
    Normalizamos para evitar falsos negativos.
    """
    if isinstance(resp_json, list):
        return resp_json
    if isinstance(resp_json, dict) and not resp_json:
        return []  # tratar {} como lista vacía
    return resp_json

@pytest.fixture
def dog_factory(base_url):
    """Crea perros y registra IDs para cleanup."""
    created_ids = []

    def _create(**overrides):
        payload = {"breed": "Labrador", "age": 3, "name": "Bobby"}
        payload.update(overrides)

        r = requests.post(f"{base_url}/dogs", json=payload, timeout=4)
        assert r.status_code in (200, 201), f"POST /dogs => {r.status_code}, body={r.text}"
        data = r.json()
        did = data.get("id") or data.get("dog_id") or data.get("uuid")
        assert did is not None, f"Response should contain an id. Got: {data}"
        created_ids.append(did)
        return did, data

    yield _create

    # cleanup best effort
    for did in created_ids:
        try:
            requests.delete(f"{base_url}/dogs/{did}", timeout=3)
        except Exception:
            pass

@pytest.fixture
def norm():
    return _normalize_list_response