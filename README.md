# LushLyrics Secured Django


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Jesulayomy/Lushlyrics-secure.git
$ cd lushlyrics-webapp-django-main
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(.venv)$ pip install -r requirements.txt
```
Note the `(.venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies, for a fresh install, run the following commands to make migrations and create a superuser:

```sh
(.venv)$ python manage.py makemigrations
(.venv)$ python manage.py migrate
(.venv)$ python manage.py createsuperuser
```

Then run the server:
```sh
(.venv)$ python manage.py runserver
```

When locally running with `DEBUG = False`, you will need to run the server with the `--insecure` flag:

```python
# settings.py
DEBUG = False
```

```sh
(.venv)$ python manage.py runserver --insecure
``` 

And navigate to `http://127.0.0.1:8000/`.
