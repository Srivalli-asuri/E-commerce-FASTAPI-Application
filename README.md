-----------------------
 --E-commerce Project --  
-----------------------

A FastAPI based E-commerce backend with PostgreSQL database, JWT authentication, RBAC (Role-based access control), and logging. Supports CRUD operations for Users, Products, Categories, and Cart functionality. Pagination is implemented using fastapi-pagination.

-------------------
Table of Contents ::
--------------------
Features

Tech Stack

Setup Instructions

Running the Server

API Endpoints

Logging

Notes
---------------------------------------
Features :
--------
User registration and login with JWT authentication

Role-based access control (admin vs user)

Product management (CRUD)

Category management (CRUD)

Cart management (Add, Edit, Delete)

Soft and hard delete for users

Pagination for users and products


Tech Stack
-----------
Framework: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Authentication: JWT (python-jose), Password hashing (argon2)

Environment Variables: python-dotenv

Logging: Python logging module 

Pagination: 
----------
fastapi-pagination




Setup Instructions

Clone the repository

git clone <repo_url>
cd   "E-commerce Project"


Create virtual environment

python -m venv venv311


Activate virtual environment

Windows:

venv311\Scripts\activate


Linux/Mac:

source venv311/bin/activate


Install dependencies

pip install -r requirements.txt


Set environment variables in .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/db_name
SECRET_KEY=your_secret_key


Create database tables

Then run:
python main.py

Running the Server
python main.py


Server will run at:

http://127.0.0.1:8000


Swagger docs available at:

http://127.0.0.1:8000/docs


API Endpoints
-------------
Auth

POST /auth/register – Register new user

POST /auth/login – Login, get JWT token

GET /auth/me – Get current logged-in user

Admin
------

GET /admin/users – Get all users (paginated)

GET /admin/users/{id} – Get single user by ID

PUT /admin/users/{id} – Update user role

DELETE /admin/users/{id} – Delete user (soft/hard)

Products
-----------

GET /products – List products (paginated)

GET /products/{id} – Get product by ID

POST /products – Add product (admin only)

PUT /products/{id} – Update product (admin only)

DELETE /products/{id} – Delete product (admin only)

Categories
---------------

GET /categories – List categories

POST /categories – Add category (admin only)

PUT /categories/{id} – Update category (admin only)

DELETE /categories/{id} – Delete category (admin only)

Cart
-------

POST /cart/add_to_cart – Add product to cart

PUT /cart/edit_cart{id} – Edit cart

DELETE /cart/delete_cart{id} – Delete cart


Logging
--------
Logs are stored in logs/app.log

Rotating file handler with max size 5 MB and 3 backups

Logs all important user and admin actions



Notes
------

Use Postman or Swagger to test APIs.

Admin user role is required for managing products, categories, and other users.

Users can only view products and manage their cart.

Soft delete for users preserves data while marking the user as deleted.

JWT tokens expire in 30 minutes by default.

This README covers project setup, folder structure, endpoints, and running instructions in an easy-to-understand way.
