# Product Price & Comparison Tool

A web application that allows users to track product prices across multiple sources, compare prices, monitor price history, and set price drop alerts.

---

## Project Structure

```
Project/
└── Backend/
    ├── main.py            # FastAPI app entry point
    ├── database.py        # MySQL connection utility
    ├── models.py          # Database table creation
    ├── schemas.py         # Pydantic request/response models
    └── routes/
        ├── __init__.py
        └── auth.py        # Authentication routes (register & login)
```

---

## Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Backend  | Python, FastAPI         |
| Database | MySQL                   |
| ORM/DB   | mysql-connector-python  |
| Validation | Pydantic              |

---

## Database Schema

Six tables are auto-created on startup via `models.py`:

| Table           | Purpose                                              |
|-----------------|------------------------------------------------------|
| `users`         | Stores registered user accounts                      |
| `products`      | Stores product names, URLs, and images               |
| `price_sources` | Stores price sources (e.g., Amazon, Flipkart) per product |
| `price_history` | Tracks historical price records per product          |
| `watchlists`    | Links users to products they are watching            |
| `alerts`        | Stores price drop alert thresholds set by users      |

---

## API Endpoints

### General

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Welcome message          |
| GET    | `/health` | Health check             |

### Authentication

| Method | Endpoint    | Description                        |
|--------|-------------|------------------------------------|
| POST   | `/register` | Register a new user                |
| POST   | `/login`    | Login with email and password      |

#### Register — Request Body
```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "yourpassword"
}
```

#### Login — Request Body
```json
{
  "email": "john@example.com",
  "password": "yourpassword"
}
```

---

## Setup & Running

### Prerequisites

- Python 3.10+
- MySQL running locally with a database named `Project_Product`

### Install Dependencies

```bash
pip install fastapi uvicorn mysql-connector-python pydantic[email]
```

### Configure Database

Update `Backend/database.py` with your MySQL credentials if different from the defaults:

```python
connection = mysql.connector.connect(
    user="root",
    password="root",
    database="Project_Product",
    host="localhost"
)
```

Create the database in MySQL if it doesn't exist:

```sql
CREATE DATABASE Project_Product;
```

### Run the Server

```bash
cd Backend
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

Interactive API docs (Swagger UI) are available at `http://localhost:8000/docs`.

---

## What's Been Built So Far

- FastAPI application scaffold with title and routing
- MySQL connection utility with error handling
- Auto table creation for all 6 core entities on startup
- User registration endpoint with duplicate email check
- User login endpoint with credential validation
- Pydantic schemas for input validation on auth routes

---

## Planned Features

- Password hashing (bcrypt)
- JWT-based authentication
- Product search and scraping from multiple e-commerce sources
- Price comparison across sources
- Price history tracking
- Watchlist management
- Price drop alert notifications
- Frontend interface
