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
The application should now be accessible at `http://127.0.0.1:8000/` this is main page 

from the page `http://127.0.0.1.8000/admin` you can log in as a superuser and add new books or delete existing ones.

## Additional Information

- Implemented a `Book` model with its corresponding fields.
- Added views for the `Book` model.
- Added views to `urls.py`.
- Implemented three views:
  - **index:** This view renders the `index.html` template, which is the main page of the application. It contains a link that directs the user to the book list page.
  - **get_books:** This view handles the book list page. It uses the Django Paginator to display 3 books per page. The user can navigate through the pages using the "Previous" and "Next" links. The `book_list.html` template is used to render the book list.
  - **get_book:** This view handles the book detail page. It retrieves the details of a specific book by its ID and renders the `book_detail.html` template with the book information.
- The `book_detail.html` template displays the title, author, category, price, and page count of the book.
- The `book_list.html` template displays a list of books, with each book title linked to its detail page.
- The `index.html` template is the main page of the application, which contains a link to the book list page.

## Usage

Start the development server:

```bash
python manage.py runserver
```
Access the main page at http://127.0.0.1:8000/. You will see a link to the book list page.

Click the link to go to the book list page (http://127.0.0.1:8000/books/). You will see a list of books, with 3 books displayed per page. Use the "Previous" and "Next" links to navigate through the pages.

Click on a book title to go to the book detail page (http://127.0.0.1:8000/books/<book_id>). You will see the detailed information about the selected book.

Log in to the admin panel (http://127.0.0.1:8000/admin) using the superuser credentials you created earlier. You can now add, edit, or delete books from the database.



