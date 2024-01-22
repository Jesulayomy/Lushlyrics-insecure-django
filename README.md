# LushLyrics-secure Django

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


## Changelog

The following improvements were made to the original project:

### Jan 22, 2024
- [Doc]: Steps on recreating the application
- [Style]: Html proper formatting and corrections
- [Style]: Conform all python files to pycodestyle, removed redundant files
- [Feature]: Custom error pages
- [Feature]: Added password reset feature

### Jan 21, 2024
- [Feature]: signup errors and form styling
- [Feature]: Added verbose errors for invalid user and passwords, Integrated login by extending template
- [Feature]: Restricted site access to logged in users
- [Solve]: Redirected anon user playlist to login page
- [Feature]: Logout for users
- [Auth]: User authentication and playlist pages
- [Del]: Removed extra login form

### Jan 2, 2024
- [Base]: Created files from fork


### Contributors

|                                 Lushlyrics-insecure                                            |                                     Lushlyrics-secure                                                |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| <img src="https://avatars.githubusercontent.com/u/81207056?v=4" alt="mohammedwed" width="150px"> | <img src="https://avatars.githubusercontent.com/u/113533393?s=96&v=4" alt="Jesulayomy" width="150px"> |
| [mohammedwed](https://github.com/mohammedwed)                                                      | [Jesulayomy](https://github.com/Jesulayomy)                                                          |

