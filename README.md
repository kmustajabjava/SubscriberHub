# SubscriberHub

SubscriberHub is a console-based telecom-inspired Customer Subscription Management System developed in Python using a layered architecture (Controller → Service → Repository) with a MySQL backend.

The project simulates common ISP/customer management operations including customer registration, subscription lifecycle management, payment tracking, support ticket management, and audit logging.

---

## Features

- Customer Management
- Subscription Management
- Payment Management
- Support Ticket Management
- Audit Logging
- Input Validation
- Layered Architecture
- MySQL Relational Database

---

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python
- Git
- GitHub
- VS Code

---

## Database Tables

- Customers
- Plans
- Subscriptions
- Payments
- SupportTickets
- AuditLogs

---

## Project Structure

```
SubscriberHub/
│
├── config/
├── controllers/
├── models/
├── repositories/
├── services/
├── utils/
├── sql/
├── app.py
└── README.md
```

---

## Implemented Modules

- Customer Management
- Subscription Management
- Payment Management
- Support Ticket Management
- Audit Logging

---

## Design Patterns

- Repository Pattern
- Service Layer
- MVC-inspired Architecture
- Separation of Concerns

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/kmustajabjava/SubscriberHub.git
```

2. Install dependencies

```bash
pip install mysql-connector-python
```

3. Create the MySQL database

Run the SQL scripts inside the `sql/` folder.

4. Update database credentials inside

```
config/database.py
```

5. Run the application

```bash
python app.py
```