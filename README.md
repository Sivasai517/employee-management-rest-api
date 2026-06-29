# 🚀 Employee Management REST API

A backend REST API built using **Flask**, **SQLAlchemy**, and **SQLite** to perform CRUD (Create, Read, Update, Delete) operations on employee records.

---

## 📌 Features

- ✅ Add Employee
- ✅ View All Employees
- ✅ View Employee by ID
- ✅ Update Employee
- ✅ Delete Employee
- ✅ Input Validation
- ✅ SQLite Database
- ✅ RESTful APIs
- ✅ Modular Project Structure

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- SQLAlchemy ORM
- REST API
- Git
- GitHub

---

## Project Structure

EmployeeAPI/

├── app.py

├── config.py

├── models.py

├── routes.py

├── requirements.txt

├── README.md

├── .gitignore

├── tests/

├── instance/

└── venv/

---

## Installation

```bash
git clone <repository>

cd EmployeeAPI

pip install -r requirements.txt

python app.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /employee | Add Employee |
| GET | /employees | Get All Employees |
| GET | /employee/<id> | Get Employee |
| PUT | /employee/<id> | Update Employee |
| DELETE | /employee/<id> | Delete Employee |

---

## Sample JSON

```json
{
  "name": "Sai",
  "department": "IT",
  "salary": 45000
}
```

---

## Author

PALLA SIVA SAI
