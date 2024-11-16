#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Build the project
echo "Building the project..."
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Make migrations and migrate the database
echo "Make migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collect static..."
python3.9 manage.py collectstatic --noinput --clear