import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("id" in task and "title" in task for task in data)

def test_create_task():
    new_task = {"title": "New Test Task"}
    response = client.post("/tasks", json=new_task)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Test Task"
    assert data["done"] is False

def test_update_task():
    # створюємо задачу
    create_res = client.post("/tasks", json={"title": "Update Me"})
    task_id = create_res.json()["id"]

    # оновлюємо
    update_res = client.put(f"/tasks/{task_id}", json={"title": "Updated", "done": True})
    assert update_res.status_code == 200
    updated_task = update_res.json()
    assert updated_task["title"] == "Updated"
    assert updated_task["done"] is True

def test_delete_task():
    # створюємо задачу
    create_res = client.post("/tasks", json={"title": "Delete Me"})
    task_id = create_res.json()["id"]

    # видаляємо
    delete_res = client.delete(f"/tasks/{task_id}")
    assert delete_res.status_code == 200
    assert delete_res.json() == {"message": "Task deleted"}

    # перевіряємо що більше нема
    get_res = client.get("/tasks")
    assert all(task["id"] != task_id for task in get_res.json())
