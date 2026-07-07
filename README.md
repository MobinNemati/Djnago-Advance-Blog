
📱 Django Advanced Blog & API Project
A comprehensive Django-based web application with RESTful API implementation, featuring user authentication, blog management, and advanced API capabilities.

https://img.shields.io/badge/Django-4.2-green.svg
https://img.shields.io/badge/DRF-3.14-blue.svg
https://img.shields.io/badge/Python-3.8+-yellow.svg
https://img.shields.io/badge/License-MIT-red.svg

📋 Table of Contents
Overview

Features

Technology Stack

Project Structure

Installation Guide

Local Development

Docker Setup

Configuration

Running the Application

API Documentation

Testing

Deployment Considerations

Contributing

License

🚀 Overview
This project is a fully-featured Django blog application that combines traditional server-side rendering with modern RESTful API capabilities. It implements custom user authentication, comprehensive blog management, and well-structured API endpoints with JWT and token-based authentication.

Key Highlights:
Custom User Model with email-based authentication

Blog Management with full CRUD operations

REST API built with Django REST Framework

Multiple Authentication Methods (Token, JWT, Session)

Comprehensive Testing suite

Docker Support for easy deployment

Interactive API Documentation (Swagger/ReDoc)

✨ Features
👤 User Management
Custom user model with email as the unique identifier

User registration with password validation

Email verification system

Password change functionality

User profile management

JWT and Token-based authentication

📝 Blog System
Create, Read, Update, Delete (CRUD) posts

Post categorization

Image upload support

Post status management (draft/published)

Author attribution

Date-based publishing

🔧 API Features
RESTful endpoints for Posts and Categories

Filtering, searching, and ordering capabilities

Pagination support

Custom permissions (IsOwnerOrReadOnly)

API versioning (v1)

Interactive API documentation

JWT authentication support

🧪 Testing
Comprehensive test suite

URL resolution tests

View tests

Model tests

Form tests

📦 Development Tools
Docker containerization

Environment variable management with python-decouple

Code formatting with Black

Linting with Flake8

🛠 Technology Stack
Backend
Technology	Version	Purpose
Django	4.2	Web framework
Django REST Framework	3.14	API development
Django REST Framework SimpleJWT	Latest	JWT authentication
Drf-YASG	1.21.8	API documentation
Django Filters	Latest	API filtering
Python Decouple	Latest	Environment management
Database
SQLite (Development) – Compatible with PostgreSQL/MySQL for production

Containerization
Docker & Docker Compose

Development Tools
Black – Code formatter

Flake8 – Code linter

Pillow – Image processing

Markdown – API documentation

📁 Project Structure
text
.
├── accounts/                    # User authentication app
│   ├── admin.py                # Admin configuration
│   ├── models.py               # User & Profile models
│   ├── serializers.py          # User serializers
│   ├── views.py                # User views
│   ├── urls.py                 # URL configuration
│   ├── api/
│   │   └── v1/
│   │       ├── views.py       # API views
│   │       ├── urls.py        # API URLs
│   │       └── serializers.py # API serializers
│   └── tests.py               # User tests
│
├── blog/                       # Blog application
│   ├── admin.py               # Admin configuration
│   ├── models.py              # Post & Category models
│   ├── views.py               # Blog views
│   ├── urls.py                # URL configuration
│   ├── forms.py               # Blog forms
│   ├── permissions.py         # Custom permissions
│   ├── paginations.py         # Pagination classes
│   ├── templates/             # HTML templates
│   │   └── blog/
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── post_confirm_delete.html
│   ├── tests/
│   │   ├── test_blog_model.py
│   │   ├── test_blog_views.py
│   │   ├── test_blog_urls.py
│   │   └── test_blog_form.py
│   └── api/
│       └── v1/
│           ├── views.py       # Blog API views
│           ├── urls.py        # Blog API URLs
│           └── serializers.py # Blog API serializers
│
├── core/                       # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── templates/                  # Global templates
│   └── index.html
│
├── statics/                    # Static files
│   ├── css/
│   ├── js/
│   ├── vendor/
│   └── fonts/
│
├── media/                      # User-uploaded media
├── requirements.txt           # Python dependencies
├── docker-compose.yml         # Docker configuration
├── Dockerfile                 # Docker image configuration
├── manage.py                  # Django management script
└── .env                       # Environment variables
📦 Installation Guide
🔧 Prerequisites
Python 3.8+

pip (Python package manager)

Git

Docker (optional)

🏠 Local Development Setup
1. Clone the Repository

bash
git clone https://github.com/MobinNemati/Djnago-Advance-Blog.git
cd django-blog-api
2. Create and Activate Virtual Environment

bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
3. Install Dependencies

bash
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the root directory:

bash
# .env file
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
5. Apply Database Migrations

bash
python manage.py makemigrations
python manage.py migrate
6. Create Superuser

bash
python manage.py createsuperuser
7. Collect Static Files

bash
python manage.py collectstatic
8. Run Development Server

bash
python manage.py runserver
🐳 Docker Setup
1. Build and Run with Docker Compose

bash
docker-compose up --build
2. Access the Application

Web Application: http://localhost:8000

Admin Panel: http://localhost:8000/admin

API Endpoints: http://localhost:8000/blog/api/v1/

3. Run Database Migrations Inside Container

bash
docker-compose exec backend python manage.py migrate
4. Create Superuser Inside Container

bash
docker-compose exec backend python manage.py createsuperuser
⚙️ Configuration
Core Settings
Setting	Description	Default
DEBUG	Development mode toggle	True
SECRET_KEY	Django secret key	Required
ALLOWED_HOSTS	Allowed hostnames	*
AUTH_USER_MODEL	Custom user model	accounts.User
Authentication Settings
The project supports multiple authentication methods:

Session Authentication – Browser-based login

Token Authentication – API token-based authentication

JWT Authentication – JSON Web Token authentication

Email Configuration
python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp4dev'  # or your SMTP server
EMAIL_PORT = 25
EMAIL_USE_TLS = False
For development, you can use the console backend:

python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
💻 Running the Application
Access Points
Endpoint	Description	URL
Home	Main index page	http://localhost:8000/
Admin	Django admin panel	http://localhost:8000/admin
Blog	Blog posts list	http://localhost:8000/blog/posts/
Login	User login page	http://localhost:8000/accounts/login/
API Endpoints
Method	Endpoint	Description
GET	/blog/api/v1/post/	List all posts
POST	/blog/api/v1/post/	Create a new post
GET	/blog/api/v1/post/{id}/	Retrieve a post
PUT	/blog/api/v1/post/{id}/	Update a post
PATCH	/blog/api/v1/post/{id}/	Partial update
DELETE	/blog/api/v1/post/{id}/	Delete a post
GET	/blog/api/v1/category/	List categories
Authentication Endpoints
Method	Endpoint	Description
POST	/accounts/api/v1/token/login/	Get authentication token
POST	/accounts/api/v1/token/logout/	Logout (invalidate token)
POST	/accounts/api/v1/jwt/create/	Create JWT token
POST	/accounts/api/v1/jwt/refresh/	Refresh JWT token
POST	/accounts/api/v1/jwt/verify/	Verify JWT token
API Authentication Examples
Token Authentication

bash
curl -X POST http://localhost:8000/accounts/api/v1/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
JWT Authentication

bash
curl -X POST http://localhost:8000/accounts/api/v1/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
Using Token in API Requests

bash
curl -X GET http://localhost:8000/blog/api/v1/post/ \
  -H "Authorization: Token your-token-here"
Using JWT in API Requests

bash
curl -X GET http://localhost:8000/blog/api/v1/post/ \
  -H "Authorization: Bearer your-access-token"
📚 API Documentation
The project includes interactive API documentation using drf-yasg:

Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

JSON Schema: http://localhost:8000/swagger/output.json

API Features
Filtering
bash
# Filter by category
GET /blog/api/v1/post/?category=1

# Filter by status
GET /blog/api/v1/post/?status=true

# Filter by author
GET /blog/api/v1/post/?author=1
Searching
bash
# Search in title and content
GET /blog/api/v1/post/?search=keyword
Ordering
bash
# Order by published date
GET /blog/api/v1/post/?ordering=published_date
GET /blog/api/v1/post/?ordering=-published_date
Pagination
bash
# Custom pagination with page size
GET /blog/api/v1/post/?page=1
🧪 Testing
Running Tests
bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test blog.tests

# Run specific test file
python manage.py test blog.tests.test_blog_views

# Run with verbosity
python manage.py test --verbosity=2
Test Coverage
The project includes comprehensive tests for:

Test Category	Files	Coverage
Models	test_blog_model.py	✅ Model creation, relationships
Views	test_blog_views.py	✅ URL resolution, responses
URLs	test_blog_urls.py	✅ URL patterns, reversals
Forms	test_blog_form.py	✅ Form validation, data handling
Test Structure Example
python
class TestBlogView(TestCase):
    def setUp(self):
        # Setup test data
        self.user = User.objects.create_user(...)
        self.post = Post.objects.create(...)
    
    def test_post_list_response(self):
        # Test view response
        response = self.client.get(reverse('blog:post-list'))
        self.assertEqual(response.status_code, 200)
🚀 Deployment Considerations
Production Settings
Security

Set DEBUG = False

Use a strong SECRET_KEY

Configure ALLOWED_HOSTS properly

Enable HTTPS

Database

Switch from SQLite to PostgreSQL or MySQL

Configure database connection pooling

Static & Media Files

Use CDN for static files

Configure S3 or similar for media storage

Email

Configure production SMTP server

Set up email verification flow

Performance

Enable caching (Redis/Memcached)

Use Gunicorn/uWSGI for WSGI server

Configure Nginx as reverse proxy

Sample Production Environment Variables
bash
# .env.production
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
STATIC_URL=/static/
MEDIA_URL=/media/
🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch

bash
git checkout -b feature/amazing-feature
Make your changes

Run tests

bash
python manage.py test
Format code

bash
black .
flake8 .
Commit changes

bash
git commit -m "Add amazing feature"
Push to branch

bash
git push origin feature/amazing-feature
Create Pull Request

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

📞 Support
For support, email 6ix.mobin@gmail.com or create an issue in the repository.

🙏 Acknowledgments
Django Community for the excellent framework

Django REST Framework team for API tools

All open-source libraries used in this project

Maktabkhooneh for educational inspiration

🔗 Quick Links
Resource	Link
Documentation	Read Docs
Issues	Report Issue
Changelog	View Changes
Demo	Live Demo
Made with ❤️ by Mobin Nemati

