# Weather-App-Using-Django-Rest-API

**The Weather App works on Weather24 CapeTown**

to install them:

**Django:**
                
                pip install Django

**Django Rest Framework:**

                pip install djangorestframework
                pip install markdown       # Markdown support for the browsable API.
                pip install django-filter  # Filtering support

don't forget to add Add rest_framework to your INSTALLED_APPS setting.

INSTALLED_APPS = (
    ...
    'rest_framework',
)


To install the required packages, it should be as easy as...

                $ pip install -r requirements.txt 


**Starting up Django**
When starting up django, a few commands are required to get you up and running.

                python manage.py makemigrations

                python manage.py migrate

                python manage.py createsuperuser

                python manage.py runserver



