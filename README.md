# Django Task Manager

A simple task management web application built with Django that demonstrates the basic CRUD operations: Create, Read, Update, and Delete.

## Features

- **Create Tasks:** Add tasks with a title, description, status, and due date.
- **View Tasks:** Display all tasks and view individual task details.
- **Update Tasks:** Edit existing task information.
- **Delete Tasks:** Delete tasks after a confirmation step.
- **Task Status:** Track tasks as Pending, In Progress, or Completed.
- **Status Filtering:** Filter the task list by status.
- **Overdue Indicators:** Highlight overdue tasks that are not completed.
- **Django Admin:** Manage tasks through the Django administration interface.

## Technologies Used

- Python
- Django
- SQLite
- Django ModelForm
- HTML
- Bootstrap 5

## Project Structure

```text
django-task-manager/
├── manage.py
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── tasks/
    ├── migrations/
    ├── templates/
    │   └── tasks/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/django-task-manager.git
cd django-task-manager
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Django:

```bash
pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account (optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to configure your admin account.

### 6. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

The Django admin interface is available at:

http://127.0.0.1:8000/admin/

## Database

The project uses Django's default SQLite database. The database file is created locally when migrations are applied.

## Purpose

This project demonstrates Django's Model-View-Template (MVT) architecture, model relationships with forms, URL routing, database migrations, and basic web application development.

## License

This project is intended for educational and learning purposes.
