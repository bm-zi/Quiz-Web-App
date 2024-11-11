# Project Target

This is a ract+drf project. The react app sends a query for a quiz to API and then a collection of questions for that specific quiz will be displayed in UI. Then, user can launch the quiz and completed the quiz test ans see the reasult at the end of the test. The API is build on a Django Rest Framwork and keeps all the data related to quizzes and questions. Users also can upload their own quiz into the backend server with a JSON formatted file, and then start to run that quiz.

## start building app

```bash
mkdir app
cd app
npx create-react-app react-quiz
# the react app components are provided in src folder ...
ls app/src
npm i json-server   # fake json server used in development phase
# fake server data location:
ls app/data/questions.json
```

## start building api

```bash
mkdir api
cd api
virtualenv venv
. venv/bin/activate
pip install django
django-admin startproject django_quiz_project .
python manage.py startapp django_quiz_app
pip install django-ckeditor
pip install djangorestframework
pip install django-cors-headers
```

### Configuration required to be done in settings.py

```python
INSTALLED_APPS = [
    # Other apps
    'django_quiz_app',
    'ckeditor',
    'rest_framework',
    'corsheaders',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React frontend
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
# Setup for ckeditor

# Setup for static and media files

```

### Files created/modifed for backend app

```bash
ls api/django_quiz_app       # app related file
ls api/django_quiz_project   # project related files
ls api/django_quiz_app/models.py
ls api/django_quiz_app/admin.py
ls api/django_quiz_app/serializers.py
ls api/django_quiz_app/views.py
ls api/django_quiz_project/urls.py
ls api/django_quiz_app/forms.py
# Create template
mkdir -p api/django_quiz_app/templates
ls api/django_quiz_app/templates/django_quiz_app/upload_quiz_json.html
# create script to upload quiz questions
mkdir -p api/django_quiz_app/management/
mkdir -p api/django_quiz_app/management/commands/
ls api/django_quiz_app/management/commands/import_quiz.py
```

### Migration

```bash
cd api
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
./manage.py createsuperuser
# to upload questions in json formatted file
./manage.py import_quiz /home/bmzi/Dev/projects/quiz/app/data/questions.json
```
