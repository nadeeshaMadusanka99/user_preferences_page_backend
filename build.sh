#!/bin/bash

#Config the environment
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

# Make migrations and migrate the database
echo "Make migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collect static..."
python3.9 manage.py collectstatic --noinput --clear

# Creating a superadmin
python3.9 manage.py shell << EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
admin_email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
admin_password = os.environ.get('ADMIN_PASSWORD', 'adminpassword')

if not User.objects.filter(username=admin_username).exists():
    User.objects.create_superuser(username=admin_username, email=admin_email, password=admin_password)
    print(f"Superuser {admin_username} created successfully.")
else:
    print(f"Superuser {admin_username} already exists.")
EOF