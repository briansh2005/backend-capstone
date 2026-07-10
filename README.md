# Little Lemon Restaurant - Backend Capstone Project

This repository contains the backend implementation for the Little Lemon Restaurant web application, developed as part of the Meta Back-End Developer Capstone Course on Coursera. The project utilizes Django and Django REST Framework (DRF) to deliver static web content and secure, fully featured REST APIs connected to a MySQL database.

---
## 📅 APIs endpoints required for Grading

http://127.0.0.1:8000/restaurant/booking/          `GET`
http://127.0.0.1:8000/restaurant/booking/tables/   `GET`

http://127.0.0.1:8000/restaurant/api-token-auth/   `POST`
http://127.0.0.1:8000/restaurant/api/users/        `POST`

#### these screen captures are also included for reference in outer project folder
---

## 🔧 Database Setup (`my.cnf`)
The project reads dynamic system configurations safely via a local initialization connection file. Ensure a configuration file exists in your project workspace mimicking this format:

```ini
[client]
database=backend_capstone
user=root
password=root@123
default-character-set=utf8
```




## 🚀 Key Features
* **Django Web Framework**: Serves static HTML template content seamlessly.
* **RESTful API Architecture**: Exposes comprehensive API endpoints for menu items and table bookings.
* **Token Authentication & User Management**: Secure user registration, authentication, and view protection powered by DRF and Djoser.
* **Relational Database**: Fully integrated with a production-ready local MySQL database server.
* **Automated Unit Testing**: Includes custom model assertions ensuring precise application formatting rules.

---

## 🛠 Tech Stack & Core Packages
* **Python**: `3.11`
* **Django**: `5.2.16` (or your active version)
* **djangorestframework**: `3.17.1` (REST framework tools)
* **mysqlclient**: `2.2.8` Database engine client wrapper for MySQL connections
* **djoser**: `2.3.3` Automated REST authentication views for handling user flows

---

## 🌐 API Endpoint Registry

All APIs are prefixed under the application path `/restaurant/`.

### 📖 Menu API (Public Views)

| Endpoint | Method | Description | Authentication |
| :--- | :--- | :--- | :--- |
| `/restaurant/menu/items/` | `GET` | Retrieve list of all menu items | None |
| `/restaurant/menu/items/` | `POST` | Create a new menu item | None |
| `/restaurant/menu/items/<int:pk>/` | `GET` | Fetch details of a single item | None |
| `/restaurant/menu/items/<int:pk>/` | `PUT` / `DELETE` | Update or destroy a menu item | None |

### 📅 Booking & User APIs (Protected Views)

| Endpoint | Method | Description | Authentication Required |
| :--- | :--- | :--- | :--- |
| `/restaurant/api/users/` | `POST` | Register a new application user | None / AllowAny |
| `/restaurant/api-token-auth/` | `POST` | Exchange username/password for a valid Token | None |
| `/restaurant/booking/tables/` | `GET` | View all active table reservations | **Token Authentication** |
| `/restaurant/booking/tables/` | `POST` | Submit a new table booking record | **Token Authentication** |
| `/restaurant/message/` | `GET` | Check auth status via protected string | **Token Authentication** |


---

## 🧪 Quick Start & Verification Commands

1. **Apply Server Migrations**:
   ```bash
   python manage.py migrate
   ```
2. **Execute Unit Tests**:
   ```bash
   python manage.py test
   ```
3. **Spin Up Development Server**:
   ```bash
   python manage.py runserver
   ```
