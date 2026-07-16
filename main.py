from fastapi import FastAPI

tasks = [
    {"id": 1, "title": "Task 1", "description": "This is task 1", "completed": False},
    {"id": 2, "title": "Task 2", "description": "This is task 2", "completed": True},
    {"id": 3, "title": "Task 3", "description": "This is task 3", "completed": False}
]

app = FastAPI()

@app.get('/'): 
    #TODO return details

@app.get('/health'):
    return {"status": "healthy"}

@app.get('/tasks'):
    return tasks


