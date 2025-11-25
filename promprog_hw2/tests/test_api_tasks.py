from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_task_crud_flow_and_validation() -> None:
    r = client.post(
        "/tasks",
        json={"title": "Write tests", "description": "pytest", "due_date": None},
    )
    assert r.status_code == 201
    task = r.json()
    assert task["title"] == "Write tests"
    task_id = task["id"]
    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 200
    r = client.get("/tasks")
    assert r.status_code == 200
    assert any(t["id"] == task_id for t in r.json())
    r = client.put(f"/tasks/{task_id}", json={"status": "done"})
    assert r.status_code == 200
    assert r.json()["status"] == "done"
    r = client.put(f"/tasks/{task_id}", json={"status": "finished"})
    assert r.status_code == 422
    r = client.get("/tasks/999999")
    assert r.status_code == 404
    r = client.delete(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.json() == {"ok": True}
