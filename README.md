# Employee Management REST API

## Overview

Employee Management REST API is a backend application built using Flask and SQLAlchemy. It provides CRUD operations for managing employee records using a SQLite database.

---

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- REST API
- JSON

---

## Features

- Add Employee
- View All Employees
- View Employee by ID
- Update Employee
- Delete Employee
- Input Validation

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
