# terogae project

Tero GAE (Google app Engine) uses:
    - Django 1.10
    - djangae 0.9.7
    - Werkzeug (provided by django-extensions).
        Since djangae doesn't have './manage.py runserver', and djangae just
        works through wsgi, we wrap the wsgi application with DebuggedApplication
        More info: https://nvbn.github.io/2015/07/17/wekzeug-django-gae/