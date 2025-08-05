📝 Django Blog Website
This is a fully functional Django-based Blog Website where users can view blog posts, explore categories, and interact via a contact form. The project is built using Django's robust MVC architecture and follows best practices for clean and scalable web development.

🚀 Features
📰 List and detail view of blog posts

🗂️ Blog categorization with Django models

📬 Contact form with form validation

🛠️ Django admin panel for managing posts and categories

🎨 Bootstrap-styled frontend

✅ CSRF protection and form validation

📁 Static files support (CSS, JS)

🏗️ Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Tools: Django Admin, Python logging

🔧 Setup Instructions

1: Clone the repository

bash
git clone https://github.com/Sanjay-D-works/Django-Project.git

cd your-repo-name

2: Create and activate a virtual environment

bash

python -m venv env

env\Scripts\activate  # On Windows

3: Install dependencies

bash

pip install -r requirements.txt

4: Apply migrations

bash

python manage.py migrate

5: Run the development server

bash

python manage.py runserver

6: Open your browser and go to:

http://127.0.0.1:8000/


📂 Project Structure (Simplified)

Django-Project/

├── blog/              # App with models, views, templates

├── Blogs/             # Project config (settings, urls)

├── templates/         # HTML templates

├── static/            # CSS, JS, images

├── manage.py

✅ Status
✔️ Completed — Ready for deployment or further customization
