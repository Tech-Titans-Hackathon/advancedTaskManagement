# Project Brief: Advanced Task Management Tool

# Project Setup Guide

## Prerequisites
Ensure you have the following installed on your system:

- Python (>= 3.8)
- pip (latest version recommended)
- virtualenv (optional but recommended)
- PostgreSQL/MySQL (if using a database other than SQLite)

## Clone the Repository
```sh
git clone <your-repo-url>
cd <your-project-name>
```

## Create and Activate Virtual Environment
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

## Install Dependencies
```sh
pip install -r requirements.txt
```

## Configure Environment Variables
Create a `.env` file in the root directory and add the required variables:
```
DEBUG=True
SECRET_KEY=<your-secret-key>
DATABASE_URL=<your-database-url>
```

## Apply Migrations
```sh
python manage.py migrate
```

## Create Superuser (Optional)
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

## Run the Development Server
```sh
python manage.py runserver
```
Access the project at: `http://127.0.0.1:8000/`

## Running Tests
```sh
python manage.py test
```

## Static Files & Media (If applicable)
```sh
python manage.py collectstatic
```

## Deployment Steps (Basic Guide)
- Set `DEBUG=False` in `.env`
- Configure `ALLOWED_HOSTS`
- Set up a production database
- Use Gunicorn/Uvicorn as WSGI/ASGI server
- Configure a reverse proxy (NGINX/Apache)

## Additional Notes
- Ensure `.env` is included in `.gitignore`
- For detailed documentation, check the `README.md` in the project
