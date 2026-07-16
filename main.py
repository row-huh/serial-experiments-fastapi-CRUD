from http.client import HTTPException

from fastapi import FastAPI

tasks = [
    {"id": 1, "title": "Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "completed": True},
    {"id": 3, "title": "Task 3", "completed": False}
]

app = FastAPI()

@app.get('/')
def root():
    return {"name": "TaskAPI", "version": "1.0.0"}

@app.get('/health')
def health():
    return {"status": "ok"}

@app.get('/tasks')
def get_tasks():
    return tasks

@app.get('/tasks/{task_id}')
def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return task
    return {"error": "Task not found"}


@app.post('/tasks/{title}')
def add_task( title:str ):
    if not title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")


    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    return new_task



# put tasks 
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskUpdate):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if updated.title is None and updated.completed is None:
        raise HTTPException(
            status_code=400,
            detail="Request body must contain title or completed"
        )

    if updated.title is not None:
        if not updated.title.strip():
            raise HTTPException(status_code=400, detail="Title cannot be empty")
        task["title"] = updated.title

    if updated.completed is not None:
        task["completed"] = updated.completed

    return task