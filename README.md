# Django microservice auth SDK

# Django auth DB router.

Simple database router that helps to split your main database and authentication database.
This may be necessary when splitting a project into microservices.

---


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
