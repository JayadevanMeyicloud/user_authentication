# user_authentication_authorization
# User Management API

A FastAPI-based User Management API with JWT Authentication, Role-Based Authorization, CRUD Operations, Pagination, Logging, and PostgreSQL integration.

---

# Features

* User Registration
* User Login
* JWT Authentication
* Role-Based Authorization
* Full User Update (PUT)
* Partial User Update (PATCH)
* Delete User
* Pagination Support
* Logging System
* PostgreSQL Database Integration

---

# Tech Stack

* Python
* FastAPI
* PostgreSQL
* Psycopg
* Pydantic
* JWT Authentication

---

# Project Structure

```bash
USER_MANAGEMENT_API/
│
├── app/
│   │
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── models/
│   │   └── user_models.py
│   │
│   ├── repository/
│   │   └── user_repository.py
│   │
│   ├── routers/
│   │   ├── auth_router.py
│   │   └── user_router.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   └── user_services.py
│   │
│   └── utils/
│       ├── auth.py
│       ├── constants.py
│       ├── dependencies.py
│       ├── exceptions.py
│       ├── logger.py
│       └── response.py
│
├── logs/
│   └── app.log
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/JayadevanMeyicloud/user_authentication.git
```

## Navigate to Project

```bash
cd USER_MANAGEMENT_API
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Server runs at:

```bash
http://127.0.0.1:8000
```

Swagger Documentation:

```bash
http://127.0.0.1:8000/docs
```

---

# Authentication APIs

| Method | Endpoint         | Description   |
| ------ | ---------------- | ------------- |
| POST   | `/auth/register` | Register User |
| POST   | `/auth/login`    | Login User    |

---

# User APIs

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/users`      | Get All Users       |
| GET    | `/users/{id}` | Get User By ID      |
| PUT    | `/users/{id}` | Full Update User    |
| PATCH  | `/users/{id}` | Partial Update User |
| DELETE | `/users/{id}` | Delete User         |

---

# Pagination Example

```bash
GET /users?page=1&limit=5
```

## Pagination Logic

```python
offset = (page - 1) * limit
```

Example:

| Page | Limit | Offset | Records |
| ---- | ----- | ------ | ------- |
| 1    | 5     | 0      | 1 → 5   |
| 2    | 5     | 5      | 6 → 10  |
| 3    | 5     | 10     | 11 → 15 |

---

# Logging

Application logs are stored in:

```bash
logs/app.log
```

Example:

```bash
2026-05-29 INFO - Login successful
2026-05-29 INFO - Users fetched successfully
2026-05-29 ERROR - Invalid password
```

---

# Authorization

This project supports role-based authorization.

Example roles:

* admin
* employee

Admin-only APIs are protected using dependency injection.

---

# PATCH API Example

```json
{
  "username": "kanmani",
  "email": "kanmani@gmail.com"
}
```

Only provided fields will be updated.

---


# Author

Jayadevan
