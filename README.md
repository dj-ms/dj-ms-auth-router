# Django microservice auth SDK

[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)

# Django auth DB router.

Simple database router that helps to split your main database and authentication database.
This may be necessary when splitting a project into microservices.
Let's say you have some Django project and want to split it into microservices.
But all of your microservices need to use the same authentication database.
This router will help you to do that.

---


## How it works
Django project that provides authentication also shares some database with other microservices.
Other microservices may have their own databases, but they all use the same authentication database.
Let's look how this scheme looks like:
<p align="center">
  <img src="docs/media/scheme.png" alt="How it works" align="center">
</p>

This is an example from [dj-ms](https://github.com/dj-ms/dj-ms-core) project.
Follow the link to explore more.


## Quickstart

Add `ms_auth_router` to your `INSTALLED_APPS` setting like this:
```python
INSTALLED_APPS = [
    ...,
    'ms_auth_router',
    ...
]
```

Add `DATABASE_ROUTERS` setting in `settings.py` file or append to existing list:
```python
DATABASE_ROUTERS = [
    'ms_auth_router.routers.DefaultRouter',
    ...
]
```

Add `auth_db` section to `DATABASES`:
```pycon
DATABASES = {
   ...
   'auth_db': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'auth.sqlite3',
   },
   ...
}
```

Finally, add `AUTH_DB` setting:
```python
AUTH_DB = 'auth_db'
```

Without this setting router will use `default` db connection.
