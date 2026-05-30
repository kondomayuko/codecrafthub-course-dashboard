# CodeCraftHub

A beginner-friendly Learning Management Platform built with Flask and REST APIs.

CodeCraftHub allows developers to track courses they want to learn, update progress, and manage their learning journey using a simple JSON file for storage.

This project is designed to help beginners learn:

* Flask
* REST APIs
* CRUD operations
* JSON data handling
* Frontend-to-backend communication

---

## Features

* View all courses
* Add new courses
* Edit existing courses
* Delete courses
* Course statistics endpoint
* JSON file storage (no database required)
* Responsive user interface
* Loading indicators
* Error handling and validation

---

## Technology Stack

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript

### Storage

* JSON file (`courses.json`)

---

## Project Structure

```text
CodeCraftHub/
│
├── app.py
├── courses.json
├── requirements.txt
├── README.md
└── index.html
```

### Files

| File             | Description           |
| ---------------- | --------------------- |
| app.py           | Flask REST API        |
| courses.json     | Stores course data    |
| index.html       | Frontend dashboard    |
| requirements.txt | Python dependencies   |
| README.md        | Project documentation |

---

## Course Data Model

Each course contains:

```json
{
  "id": 1,
  "name": "Python Flask Basics",
  "description": "Learn Flask REST APIs",
  "target_date": "2026-07-15",
  "status": "In Progress",
  "created_at": "2026-05-30T10:00:00"
}
```

### Field Descriptions

| Field       | Description                         |
| ----------- | ----------------------------------- |
| id          | Auto-generated unique identifier    |
| name        | Course name                         |
| description | Course description                  |
| target_date | Target completion date              |
| status      | Not Started, In Progress, Completed |
| created_at  | Timestamp generated automatically   |

---

# Installation

## Step 1: Clone the Project

```bash
git clone https://github.com/yourusername/CodeCraftHub.git
cd CodeCraftHub
```

Or create a new project folder manually.

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install flask
```

---

## Step 4: Save Dependencies

```bash
pip freeze > requirements.txt
```

---

# Running the Application

Start the Flask server:

```bash
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# API Documentation

Base URL:

```text
http://localhost:5000/api/courses
```

---

## Create Course

### Request

```http
POST /api/courses
```

### Body

```json
{
  "name": "Python Flask Basics",
  "description": "Learn Flask APIs",
  "target_date": "2026-07-15",
  "status": "Not Started"
}
```

### Response

```json
{
  "id": 1,
  "name": "Python Flask Basics",
  "description": "Learn Flask APIs",
  "target_date": "2026-07-15",
  "status": "Not Started",
  "created_at": "2026-05-30T10:00:00"
}
```

---

## Get All Courses

### Request

```http
GET /api/courses
```

### Response

```json
[
  {
    "id": 1,
    "name": "Python Flask Basics",
    "description": "Learn Flask APIs",
    "target_date": "2026-07-15",
    "status": "Not Started",
    "created_at": "2026-05-30T10:00:00"
  }
]
```

---

## Get Course by ID

### Request

```http
GET /api/courses/1
```

### Response

```json
{
  "id": 1,
  "name": "Python Flask Basics",
  "description": "Learn Flask APIs",
  "target_date": "2026-07-15",
  "status": "Not Started",
  "created_at": "2026-05-30T10:00:00"
}
```

---

## Update Course

### Request

```http
PUT /api/courses/1
```

### Body

```json
{
  "status": "Completed"
}
```

### Response

```json
{
  "id": 1,
  "name": "Python Flask Basics",
  "description": "Learn Flask APIs",
  "target_date": "2026-07-15",
  "status": "Completed",
  "created_at": "2026-05-30T10:00:00"
}
```

---

## Delete Course

### Request

```http
DELETE /api/courses/1
```

### Response

```json
{
  "message": "Course deleted successfully."
}
```

---

## Course Statistics

### Request

```http
GET /api/courses/stats
```

### Response

```json
{
  "total_courses": 4,
  "status_counts": {
    "Not Started": 1,
    "In Progress": 1,
    "Completed": 2
  }
}
```

---

# Testing

## Add Course

```bash
curl -X POST http://localhost:5000/api/courses \
-H "Content-Type: application/json" \
-d '{
"name":"Python Flask Basics",
"description":"Learn Flask APIs",
"target_date":"2026-07-15",
"status":"Not Started"
}'
```

---

## Get Courses

```bash
curl http://localhost:5000/api/courses
```

---

## Get Single Course

```bash
curl http://localhost:5000/api/courses/1
```

---

## Update Course

```bash
curl -X PUT http://localhost:5000/api/courses/1 \
-H "Content-Type: application/json" \
-d '{
"status":"Completed"
}'
```

---

## Delete Course

```bash
curl -X DELETE http://localhost:5000/api/courses/1
```

---

## Get Statistics

```bash
curl http://localhost:5000/api/courses/stats
```

---

# Common Error Responses

## Missing Required Field

```json
{
  "error": "Missing required field: description"
}
```

---

## Invalid Status

```json
{
  "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

---

## Invalid Date Format

```json
{
  "error": "Invalid target_date format. Use YYYY-MM-DD."
}
```

---

## Course Not Found

```json
{
  "error": "Course not found."
}
```

---

# Troubleshooting

## Flask Not Installed

Error:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
pip install flask
```

---

## Port Already in Use

Error:

```text
Address already in use
```

Solution:

```python
app.run(debug=True, port=5001)
```

---

## JSON File Missing

The application automatically creates:

```text
courses.json
```

if it does not already exist.

---

## API Connection Errors

Make sure Flask is running before opening the frontend:

```bash
python app.py
```

---

# Learning Objectives

This project helps beginners learn:

* REST API fundamentals
* CRUD operations
* HTTP methods
* Flask routing
* JSON serialization
* Form handling
* Error handling
* Frontend and backend integration

---

# Future Improvements

Potential enhancements:

* SQLite database
* User authentication
* Search and filtering
* Pagination
* Swagger/OpenAPI documentation
* Docker deployment
* Unit testing with pytest
* User accounts and progress tracking

---

# License

This project is intended for educational and learning purposes.
