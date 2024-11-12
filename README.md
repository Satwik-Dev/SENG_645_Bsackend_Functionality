# UMBC Retriever Essentials – Smart Grocery & Food Waste App

This project is a web-based inventory management system developed for the Retriever Essentials program at UMBC. It aims to support food inventory tracking, expiration alerts, and meal recommendations for students. The system is structured with two primary user roles: administrators, who manage inventory, and students, who monitor and control their inventory usage.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [User Roles](#user-roles)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

---

## Features

- **Inventory Management**: Track items with categories, quantities, and expiration dates.
- **Expiration Alerts**: Notify users about items that are close to expiration.
- **AJAX Integration**: Real-time updates for quantity adjustments and inventory filtering without reloading the page.
- **Barcode or Manual Entry**: Admins can add or update items in the inventory either by scanning a barcode or using manual entry.
- **Role-Based Access**: 
  - **Admin**: Full access to manage the inventory, including adding, updating, and deleting items.
  - **Student**: Limited access to view inventory items and track their usage.

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, AJAX
- **Backend**: Django, Python
- **Database**: SQLite (for structured data), MongoDB (for unstructured or scalable data, such as logs or history)
- **Environment**: Virtual environment (recommended)

---

## Project Structure

```plaintext
retriever_essentials_umbc/
├── client/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── client/
│           ├── admin_dashboard.html
│           ├── student_dashboard.html
│           └── client_page.html
├── inventory/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── inventory/
│           ├── inventory_list.html
│           └── update_inventory.html
├── retriever_essentials_umbc/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates/
    ├── login.html
    ├── password_reset_form.html
    ├── password_reset_done.html
    ├── password_reset_confirm.html
    └── password_reset_complete.html

## Installation
- **Clone the Repository**:
git clone https://github.com/yourusername/retriever_essentials.git
cd retriever_essentials

##Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows, use venv\\Scripts\\activate

##Install Dependencies:
pip install -r requirements.txt

##Configure the Database:
By default, the project uses SQLite for structured data and MongoDB for unstructured data.
Make sure MongoDB is installed and running on your system if you plan to use it for logs or other scalable data.

##Apply Migrations:
python manage.py makemigrations
python manage.py migrate

##Run the Server:
python manage.py runserver
The application will be available at http://127.0.0.1:8000.
