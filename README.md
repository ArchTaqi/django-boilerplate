# Django Boilerplate

Boilerplate to use when starting new Django 3 projects with PostgreSQL.

- Django 3.0 
- Python 3.9 
- PostgreSQL 13
- gunicorn 
- whitenoise in case of Heroku
- dj-database-url
- and a free Heroku hobby dyno (name for a Linux container in which your app will run).

##Contributing

Feel free to add other settings that I might've missed out, and send me a PR.


## Usage

Start a new project using this template:

```
django-admin.py startproject --template=https://github.com/muhammadtaqi/django-boilerplate/archive/latest.zip --extension=py,gitignore project_name
```

Install requirements via pip:

```
pip install -r requirements.txt
```

Run database migrations:

```
python manage.py migrate
```

## Deploy to Heroku

**Step 1: Add a Procfile**

- The Procfile (compressed version of "process file") tells the dyno (Linux container that Heroku creates for you) what to do with your app. You can [add multiple process types][1] to your Procfile.
- In your **project root**, create a file called `Procfile` (capital "P", no extensions) and add the following line of code to it:

`web: gunicorn config.wsgi.heroku —-log-file -`

* `web: gunicorn `is telling your dyno to run a web process with gunicorn.
* `django-heroku.wsgi` is telling the dyno to look in a file called `wsgi` in the folder called `sampledeploy` — substitute this with the name of your project.
* `—-log-file -` is saying add the output to the logs

`gunicorn` is an abbreviation for "Green Unicorn" and it's a sort of translator/courier that sits between the server and your web app when there's a need to show dynamic content. When the server gets a request from the end user's browser that involves some dynamic content, it calls gunicorn, which takes HTTP packets from the server, translates them into a Web Service Gateway interface (that's the WSGI!) readable format, and fires it over to your web framework (Django) to process. When it's ready, the framework sends an HTTP request back to the server via gunicorn, and the server sends that data back to the end user's browser.

WSGI is a standard communication spec for enabling web servers and applications to communicate with one another.

Your `Procfile` won't work unless you've installed gunicorn via the `requirements.txt` file in the sample app or `pip install gunicorn` in your terminal.

**Step 2: Creating a heroku app**

- Sign into Heroku by typing `heroku login` and your credentials.
- Create our Heroku app! Type `heroku create app_name`.

To avoid some common issues before you begin, make sure that:

* Both `requirements.txt` and `Procfile` files are in your project root, the same directory as `manage.py`. If they are not, the paths get messed up and you'll get an error saying your app can't be found.
- Add the Heroku URL to our list of `ALLOWED_HOSTS` like this: `ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'app_name.herokuapp.com']` in `settings.py`.

To run locally, 
`heroku local web`
Then push to heroku
`git push heroku master`

**Step 3: Set environment variables in Heroku**

`heroku config:set SECRET_KEY=RaNdOmStrInG DJANGO_SETTINGS_MODULE=config.settings.heroku DISABLE_COLLECTSTATIC=1`
`heroku ps:scale web=1`

At this point, it's a good idea to add any other environment variables you were using locally.

**Step 4: Set up your database on Heroku**

`heroku addons:create heroku-postgresql:hobby-dev`
`heroku addons:create heroku-redis:hobby-dev`

In the terminal, like this:

`heroku run python manage.py makemigrations`
`heroku run python manage.py migrate`
`heroku run python manage.py createsuperuser`

**Step 5: Whitenoise and static file set up**

- Whitenoise is a Python package that enables your Django app to serve its own static files (like images), so you don't need to worry about setting them up on Amazon S3 or anything like that. It can be slower to do it this way, but it is really convenient. If you prefer to serve your static files from another source, you can skip this section.
- Whitenoise is in the `requirements.txt` in the sample app, but if you aren't starting with that, type `pip install whitenoise` in the terminal.
- Add a `static` folder in our `project root`.

In the `settings.py` file, add the following:

* Add this to the `MIDDLEWARE` list after the security middleware: `whitenoise.middleware.WhiteNoiseMiddleware,`.
* Add this line wherever you like (I usually put it with my other `STATIC` variables): `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`&nbsp;.
* If you want to run Whitenoise in development (which I recommend just to make sure you don't see different behavior in production), add this before the `django.contrib.staticfiles` item in your `INSTALLED_APPS` list: `'whitenoise.runserver_nostatic'`&nbsp;. You can also run your local server by typing `python manage.py runserver --nostatic`&nbsp;, but you need to do that every time — adding that line is less error prone.

Now, 

* At the top of the html file, tell Django to load the static files:`{% load static %}` and add files like this `<img src="{% static " img="" field.jpg"="" alt="image of a field at dusk" %}"="">`


[1]: https://devcenter.heroku.com/articles/procfile
[2]: http://ivory.idyll.org/articles/wsgi-intro/what-is-wsgi.html