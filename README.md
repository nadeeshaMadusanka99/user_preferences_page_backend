# User Preferences Management System

## Overview
This project is a **User Preferences Management System** built with Django and Django Rest Framework (DRF) for handling user-specific preferences like Account Settings, Notification Settings, Privacy Settings, and Theme Settings.

## Key Features:
- **User Types**: The system supports two user types: Super Admins with full access and Normal Users who can manage their own preferences.
- **User Preference Management**: Users can update their account settings, privacy settings, notification preferences, and theme settings.
- **Validation**: Enforces constraints to prevent multiple preference objects for the same user.
- **RESTful API**: Exposes endpoints for handling user preferences using Django Rest Framework.
- **Robust Error Handling**: Handles common errors like permission denial, object not found, and validation errors.

## Installation

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nadeeshaMadusanka99/user_preferences_page_backend.git
   cd <project-directory>
2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run migrations:
    ```bash
    python manage.py migrate

5. Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser

6. Run the development server:
    ```bash
    python manage.py runserver
    
The app should now be running at http://localhost:8000.

## Testing 
### Testing Strategy:
- **Unit Tests**: Test individual components of the app (models, views).
- **Functional Tests**: Test user workflows, including error validations.

### Test Coverage:
- Used `django.test` for running tests.
- The app is tested against common edge cases, authentication errors, and valid/invalid data inputs.
- To run the tests, use:
   ```bash
   python manage.py test test.preferences

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


