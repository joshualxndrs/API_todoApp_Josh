from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str
    completed: bool


tasks = {
    1: {
        "name": "Math",
        "description": "Calculus",
        "completed": True
    }
}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return tasks.get(task_id)


@app.get("/tasks-by-name")
def get_task_by_name(name: str):
    for task_id, task in tasks.items():
        if task["name"] == name:
            return {task_id: task}
    return {"message": "Task not found"}


@app.post("/tasks/{task_id}")
def add_task(task_id: int, task: Task):
    if task_id in tasks:
        return {"message": "Task already exists"}
    tasks[task_id] = task.dict()
    return tasks[task_id]


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id in tasks:
        tasks[task_id].update(updated_task.dict())
        return tasks[task_id]
    return {"message": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id in tasks:
        del tasks[task_id]
        return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}
