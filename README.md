# TBC Django

This is a Django project with one app, 'market', that includes modules for books, authors, and categories. I've organized views and models into separate folders for better structure.

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
The application should now be accessible at `http://127.0.0.1:8000/` this is the main page 

From the page `http://127.0.0.1.8000/admin` you can log in as a superuser and add new books, authors, or categories, or delete existing ones.

## Additional Information

- Implemented models for `Book`, `Author`, and `Category` with their corresponding fields.
- Added views for the `Book`, `Author`, and `Category` models.
- Added views to `urls.py`.
- Implemented views for:
  - **Books:**
    - **book_list:** This view renders the book list page, displaying a paginated list of books.
    - **book_detail:** This view handles the book detail page, showing detailed information about a specific book.
  - **Authors:**
    - **author_list:** This view renders the author list page, displaying a paginated list of authors.
    - **author_detail:** This view handles the author detail page, showing detailed information about a specific author.
  - **Categories:**
    - **category_list:** This view renders the category list page, displaying a paginated list of categories.
    - **category_detail:** This view handles the category detail page, showing detailed information about a specific category.

- The templates and static files for authors and categories have been added in the respective folders.
- Updated admin panel to register models for authors and categories.

## Usage

Start the development server:

```bash
python manage.py runserver
```
Access the main page at http://127.0.0.1:8000/. You will see links to the book list, author list, and category list pages.

Click the links to go to the respective list pages:

*   Book list page: http://127.0.0.1:8000/book/
   
*   Author list page: http://127.0.0.1:8000/author/
   
*   Category list page: http://127.0.0.1:8000/category/
   

On each list page, you will see paginated lists of items. Use the "Previous" and "Next" links to navigate through the pages.

Click on an item to go to its detail page:

*   Book detail page: http://127.0.0.1:8000/book/<book_id>/
   
*   Author detail page: http://127.0.0.1:8000/author/<author_id>/
   
*   Category detail page: http://127.0.0.1:8000/category/<category_id>/
   

Log in to the admin panel (http://127.0.0.1:8000/admin) using the superuser credentials you created earlier. You can now add, edit, or delete books, authors, or categories from the database.
