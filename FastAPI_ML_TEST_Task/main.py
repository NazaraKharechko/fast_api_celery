from fastapi import FastAPI
from routers import pages  

from storage import tasks

app = FastAPI()

# --- API ---
@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {"id": new_id, "title": task["title"], "done": False}
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.get("title", task["title"])
            task["done"] = updated_task.get("done", task["done"])
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted"}


# --- Frontend ---
app.include_router(pages.router)  
