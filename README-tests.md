# AffiniPay Candidate Exercise — Test Suite (pytest)

## Requirements

* Docker Desktop (with WSL2) on Windows, or Docker on macOS/Linux.
* Python 3.12+ to run `pytest`.

---

## 1) Run the API (Docker)

```bash
docker build -t exercise:1.0 .
docker rm -f demo 2>/dev/null || true
docker run --name demo -d -p 5000:5000 exercise:1.0
```

Quick check:

```bash
curl -L http://127.0.0.1:5000/dogs/
```

---

## 2) Run the tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-tests.txt

export DOGS_BASE_URL=http://127.0.0.1:5000
pytest -q
```

---

## Local results I got

```
3 passed, 4 xfailed, 1 xpassed
```

* **passed**: list works, create+get by id works, delete returns 404/410 (depends on the implementation).
* **xfail**: validation cases marked as *expected to fail* when the API accepts invalid payloads (see below).
* **xpassed**: if the API validates one of these cases correctly, it will appear as xpassed.

---

## 3) Files I added

```
requirements-tests.txt
tests/
  conftest.py
  test_dogs_happy_path.py
  test_dogs_validation.py
  test_dogs_delete.py
README-tests.md
```

---

## 4) Notes / Findings

* **Empty list format**: `GET /dogs/` returned `{}` in my environment. For empty collections, `[]` is the usual format.
  The tests convert `{}` to `[]` so the happy path still works.
* **Input validation** (marked as `xfail`):

  * empty `breed`
  * negative or non-integer `age`
  * incomplete / empty payload
    If the API does not reject these with `400/422`, the tests stay as `xfail` (to show the possible gap) without failing the suite.
* **DELETE contract**: after deleting a dog, the test expects a `404/410` when getting it again. If the API sends another code, I documented the real behavior.

---

## 5) Troubleshooting

* **Redirect `/dogs` → `/dogs/`**: use `curl -L` or point directly to the path with the trailing slash.
* **Build error (Conda TOS)**: use the `RUN conda tos accept ...` shown in the original instructions, or change channels to `conda-forge`.
* **Port 5000 in use**:

```bash
docker rm -f demo
docker run --name demo -d -p 5001:5000 exercise:1.0
export DOGS_BASE_URL=http://127.0.0.1:5001
pytest -q
```
