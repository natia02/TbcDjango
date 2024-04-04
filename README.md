# TBC Django

it is just a template of the django project. Below you can see instructions how to use it.

## Prerequisites

- Python (version 3.12.2)
- Django (version 5.0.3)

1. Clone the repository: 
    ```bash
    git clone https://github.com/natia02/TbcDjango.git
    ```
2. Navigate to the project directory: 
    ```bash
    cd TbcDjango
    ```

3. Create and activate a virtual environment: 
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use env\Scripts\activate
    ```

4. Install the required dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

5. Run database migrations: 
    ```bash
    python manage.py migrate
    ```

6. Create a superuser: 
    ```bash
    python manage.py createsuperuser
    ```
   and follow instructions

7. Start the development server: 
    ```bash
    python manage.py runserver
    ``` 
The application should now be accessible at `http://127.0.0.1:8000/`

from the page `http://127.0.0.1.8000/admin` you can log in as a superuser.
