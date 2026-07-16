from http.client import HTTPException

from fastapi import FastAPI, status

tasks = [
    {"id": 1, "title": "Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "completed": True},
    {"id": 3, "title": "Task 3", "completed": False}
]

app = FastAPI()

@app.get('/', status_code=status.HTTP_200_OK)
def root():
    """
    Initial information about the API, including its name, version, and available endpoints.
    """
    return {"name": "TaskAPI", "version": "1.0.0", "Endpoints": {
        "GET (/)": "Get initial information about the API",
        "GET (/health)": "Check the health of the API",
        "GET (/tasks)": "Get all tasks",
        "GET (/tasks/{task_id})": "Get a specific task by ID",
        "POST (/tasks)": "Add a new task",
        "PUT (/tasks/{task_id})": "Update an existing task",
        "DELETE (/tasks/{task_id})": "Delete a task"
    }}

@app.get('/health', status_code=status.HTTP_200_OK)
def health():
    """
    Status Check
    """
    return {"status": "ok"}

@app.get('/tasks', status_code=status.HTTP_200_OK)
def get_tasks():
    """
    Retrieve all tasks.
    """
    return tasks

@app.get('/tasks/{task_id}', status_code=status.HTTP_200_OK)
def get_task(task_id: int):
    """
    Get task by an ID. If the task is not found, return an error message.
    """
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return task
    return {"error": "Task not found"}


@app.post('/tasks/{title}', status_code=status.HTTP_201_CREATED)
def add_task( title:str ):
    """
    Add a new task.
    """
    if not title.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title cannot be empty")


    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    return new_task



# put tasks 
@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, title: str = None, completed: bool = None):
    """
    Update an existing task
    """
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if title is None and completed is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request body must contain title or completed"
        )

    if title is not None:
        if not title.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title cannot be empty")
        task["title"] = title

    if completed is not None:
        task["completed"] = completed

    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    """
    Delete an existing task 
    """
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    tasks.remove(task)
    return {"message": "Task deleted successfully"}