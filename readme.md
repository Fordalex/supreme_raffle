# Supreme Raffle

### Django Allauth

Start off installing allauth:

    pip install django-allauth

Go to the documentation and add the required setting in the settings.py:

    (Documentation)[https://django-allauth.readthedocs.io/en/latest/installation.html]

Go to the project level urls.py file and add the following:

    path('accounts/', include('allauth.urls'))

Then migrate the changes:

    python3 manage.py migrate

After, login to the django admin page and update the sites name (This is required for social media authentication)

    supremeraffle.com

These are the basic variables that need to be added to the settings.py:

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = True
    ACCOUNT_USERNAME_MIN_LENGTH = 4
    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/'
    ACCOUNT_FORMS = {'signup': 'user.forms.RegistrationForm'}

Then freeze the requirement of the project:

    pip3 freeze --local > requirements.txt

To make changes to the allauth templates, the templates need to first be moved.

Make a folder called 'allauth' inside the templates directory.

Move the templates with the following command:

    cp -r .venv/lib/python3.6/site-packages/allauth/templates/* ./templates/allauth

(To find out the current vision of python, just type python in the CL)

Update the DIRS array in the settings.py:

    'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],