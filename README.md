# TBC Django

This is a Django project with one app, 'market', that includes a module called Book with its attributes and 
corresponding views. I've organized views and models into separate folders for better structure. The project is 
designed such that a superuser can add books to the database and search for books by their name and author.


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
    env\Scripts\activate
    ```

4. Install the required dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

5. Create a superuser: 
    ```bash
    python manage.py createsuperuser
    ```
   and follow instructions

6. Start the development server: 
    ```bash
    python manage.py runserver
    ``` 
The application should now be accessible at `http://127.0.0.1:8000/`

from the page `http://127.0.0.1.8000/admin` you can log in as a superuser and add new books or delete existing ones.

## Additional Information

- Implemented a Book model with its corresponding fields.
- Added views for the Book model.
- Added views to `urls.py`.
- Implemented two views:
  1. `get_books`: Returns a list of all the books. Accessible at [http://127.0.0.1:8000/books](http://127.0.0.1:8000/books).
  2. `get_book`: Returns details of a book by its ID. Accessible at [http://127.0.0.1:8000/books/<book_id>](http://127.0.0.1:8000/books/<book_id>).
- Note: Book IDs start from 3 in the database.


