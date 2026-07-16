# TaskAPI

A simple REST API built with **FastAPI** that demonstrates CRUD (Create, Read, Update, Delete) operations for managing tasks.

## Features

- Retrieve API information
- Health check endpoint
- View all tasks
- View a task by ID
- Create a new task
- Update an existing task
- Delete a task

> **Note:** This project uses an in-memory list to store tasks. Data is not persisted and will reset whenever the server restarts.

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

Install the required packages:

```bash
pip install fastapi uvicorn
```

---

## Running the API

Start the server with:

```bash
uvicorn main:app --reload
```

Replace `main` with the name of your Python file if it is different.

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## API Endpoints

### Root

**GET /**

Returns basic information about the API.

Example response:

```json
{
  "name": "TaskAPI",
  "version": "1.0.0"
}
```

---

### Health Check

**GET /health**

Checks whether the API is running.

Example response:

```json
{
  "status": "ok"
}
```

---

### Get All Tasks

**GET /tasks**

Returns all tasks.

Example response:

```json
[
  {
    "id": 1,
    "title": "Task 1",
    "completed": false
  }
]
```

---

### Get Task by ID

**GET /tasks/{task_id}**

Returns a specific task.

Example:

```
GET /tasks/1
```

---

### Create Task

**POST /tasks/{title}**

Creates a new task.

Example:

```
POST /tasks/Buy milk
```

Response:

```json
{
  "id": 4,
  "title": "Buy milk",
  "completed": false
}
```

---

### Update Task

**PUT /tasks/{task_id}**

Updates the title and/or completion status of a task.

Example:

```
PUT /tasks/2?title=Finish assignment&completed=true
```

---

### Delete Task

**DELETE /tasks/{task_id}**

Deletes a task.

Example:

```
DELETE /tasks/2
```

Response:

```json
{
  "message": "Task deleted successfully"
}
```

---

## Task Structure

Each task contains the following fields:

| Field | Type | Description |
|--------|------|-------------|
| id | integer | Unique task identifier |
| title | string | Task title |
| completed | boolean | Completion status |

---

## Project Structure

```
.
├── main.py
└── README.md
```

Replace `main.py` with your actual filename if necessary.

---

## Limitations

- Uses an in-memory Python list instead of a database.
- Task IDs are generated using the current list length.
- Data is lost whenever the server restarts.
- No authentication or authorization is implemented.

---

## Future Improvements

- Store tasks in a database (SQLite, PostgreSQL, etc.).
- Use Pydantic request models for input validation.
- Return proper HTTP status codes for all endpoints.
- Add automated tests.
- Add pagination and filtering.
- Implement authentication and user accounts.