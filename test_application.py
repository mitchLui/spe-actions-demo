from fastapi.testclient import TestClient

from application import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}


def test_add():
  response = client.get("/add?a=1&b=2")
  assert response.status_code == 200
  assert response.json() == {
    "message": "1 + 2 = 3",
    "success": True
  }

def test_subtract():
  response = client.get("/subtract?a=1&b=2")
  assert response.status_code == 200
  assert response.json() == {
    "message": "1 - 2 = -1",
    "success": True
  }
