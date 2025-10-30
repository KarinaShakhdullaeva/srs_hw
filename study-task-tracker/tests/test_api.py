def test_create_and_get_task_api(client):
    # create
    resp = client.post("/api/v1/tasks", json={"title": "Prepare lab", "description": "Physics", "due_date": None})
    assert resp.status_code == 201, resp.text
    task = resp.json()
    assert task["id"] > 0
    # get
    resp2 = client.get(f"/api/v1/tasks/{task['id']}")
    assert resp2.status_code == 200
    assert resp2.json()["title"] == "Prepare lab"
