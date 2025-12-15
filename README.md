# Green Energy Website - Django Project

A Django-based website for a green energy company featuring user authentication, contact forms, blog posts, and newsletter subscriptions.

## Features

- **User Authentication**: Registration and login functionality
- **Contact Form**: Submit inquiries with service selection
- **Blog**: Display blog posts about green energy
- **Newsletter**: Email subscription management
- **Responsive Design**: Modern UI with Tailwind CSS
- **Admin Panel**: Full admin interface for managing content

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Access the website at `http://127.0.0.1:8000/`

## Project Structure

- `myapp/`: Main application
  - `models.py`: Database models (Contact, BlogPost, Newsletter)
  - `views.py`: View functions for all pages
  - `urls.py`: URL routing
  - `admin.py`: Admin panel configuration
- `template/`: HTML templates
  - `base.html`: Base template with navigation
  - `index.html`: Homepage
  - `login.html`: Login page
  - `register.html`: Registration page
  - `contact.html`: Contact form page
  - `about.html`: About page
  - `blog.html`: Blog listing page
  - `pricing.html`: Pricing page
- `static/`: Static files (CSS, images, assets)
- `wdp/`: Django project settings

## Pages

- `/` - Homepage
- `/about/` - About us page
- `/contact/` - Contact form
- `/blog/` - Blog posts listing
- `/pricing/` - Pricing plans
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout
- `/admin/` - Django admin panel

## Models

### Contact
Stores contact form submissions with fields:
- full_name, email, company (optional), service, message (optional), created_at

### BlogPost
Manages blog posts with fields:
- title, slug, author, content, excerpt, image, category, read_time, created_at, updated_at, published

### Newsletter
Manages newsletter subscriptions with fields:
- email, subscribed_at, active

## Admin Panel

Access the admin panel at `/admin/` to:
- Manage contact submissions
- Create and edit blog posts
- Manage newsletter subscriptions
- Manage users

## Technologies Used

- Django 5.2.6
- SQLite (default database)
- Tailwind CSS (for styling)
- Alpine.js (for interactive components)

