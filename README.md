# Task Management API

## 📌 Project Overview

The **Task Management API** is a backend RESTful service built with **Django** and **Django REST Framework (DRF)**. It allows authenticated users to manage their personal tasks by creating, viewing, updating, deleting, and marking tasks as complete or incomplete.

This project simulates real-world backend development practices, including authentication, permissions, data validation, and deployment.

---

## 🚀 Features

### ✅ User Authentication

* JWT-based authentication using **Simple JWT**
* Secure login and token refresh endpoints
* Password hashing handled by Django

### ✅ Task Management (CRUD)

* Create tasks with title, description, due date, and priority
* Read a list of tasks belonging to the authenticated user
* Update tasks (restricted if task is completed)
* Delete tasks

### ✅ Task Status Management

* Mark tasks as **Completed** or **Pending**
* Automatically records timestamp when a task is completed
* Prevents editing completed tasks unless reopened

### ✅ Filtering & Sorting

* Filter tasks by:

  * Status (Pending / Completed)
  * Priority (Low / Medium / High)
  * Due Date
* Sort tasks by:

  * Due Date
  * Priority

### ✅ Task Ownership & Permissions

* Users can only access and manage their own tasks
* Custom permission class ensures data isolation

---

## 🛠 Tech Stack

* **Backend Framework:** Django
* **API Framework:** Django REST Framework (DRF)
* **Authentication:** JWT (Simple JWT)
* **Database:** SQLite (development) / PostgreSQL (production)
* **Deployment:** PythonAnywhere or Heroku

---

## 📂 Project Structure

```
task_management_api/
├── manage.py
├── task_management_api/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── admin.py
└── README.md
```

---

## 🔐 Authentication Endpoints

| Method | Endpoint              | Description                   |
| ------ | --------------------- | ----------------------------- |
| POST   | `/api/token/`         | Obtain access & refresh token |
| POST   | `/api/token/refresh/` | Refresh access token          |

**Authorization Header:**

```
Authorization: Bearer <access_token>
```

---

## 📋 Task Endpoints

| Method | Endpoint                    | Description             |
| ------ | --------------------------- | ----------------------- |
| GET    | `/api/tasks/`               | List user tasks         |
| POST   | `/api/tasks/`               | Create a new task       |
| GET    | `/api/tasks/{id}/`          | Retrieve a task         |
| PUT    | `/api/tasks/{id}/`          | Update a task           |
| DELETE | `/api/tasks/{id}/`          | Delete a task           |
| POST   | `/api/tasks/{id}/complete/` | Mark task as completed  |
| POST   | `/api/tasks/{id}/reopen/`   | Reopen a completed task |

---

## 🧪 Example Request

### Create Task

```http
POST /api/tasks/
Authorization: Bearer <token>
```

```json
{
  "title": "Finish Capstone Project",
  "description": "Complete backend API",
  "due_date": "2025-12-31",
  "priority": "HIGH"
}
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd task_management_api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start Server

```bash
python manage.py runserver
```

---

## 🔒 Security Considerations

* JWT authentication for all endpoints
* Task ownership enforced at the permission level
* Input validation handled via serializers
* Passwords securely hashed by Django

---

## 🌍 Deployment

For production:

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Use PostgreSQL database
* Deploy on **PythonAnywhere** or **Heroku**

---

## 🎯 Stretch Goals (Optional)

* Task categories (Work, Personal)
* Recurring tasks
* Task history & analytics
* Email or in-app notifications
* Collaborative task sharing

---

## 👨‍💻 Author

**Christopher Dominic Eze**
Backend Developer | Django | REST APIs

---

## 📄 License

This project is for educational and portfolio purposes.
