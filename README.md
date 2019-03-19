# voting-app
A Simple Voting System.

First we have to set up virtual environment the follow steps given below.

1. Install requirement.txt file as
    <pre> pip install -r requirements.txt </pre>

2. (Optional) Set-Up PostgreSQL database as backend with credentials as follows

    <pre>
      DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'polls1',
            'HOST': 'localhost',
            'PORT': 5432,
            'USERNAME': 'postgres',
            'PASSWORD': 'password',
        }
      }
    </pre>
  
3. Migrate your models to apply with following commands
    <pre>
      a. python manage.py makemigrations
      b. python manage.py migrate
    </pre>

4. Run app by running following command
  python manage.py runserver

Now, You can visit http://localhost:8000/ OR If you want to view detail of URL endpoints visit http://localhost:8000/docs/ 
