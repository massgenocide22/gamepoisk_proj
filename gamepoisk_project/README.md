# GamePoisk (Django)

Minimal Django project skeleton implementing:
- Game model with image uploads (via admin)
- Comment model attached to Game
- Advanced search (title, genre, developer, publisher) using __icontains and Q
- Simple login/logout using Django's auth views

## Setup

1. Create virtualenv and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Apply migrations and create superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Visit the admin at http://127.0.0.1:8000/admin/ to add Games (you can upload images here).

## Notes
- MEDIA files are served automatically in DEBUG mode.
- This is a skeleton for learning and should be hardened before production.
