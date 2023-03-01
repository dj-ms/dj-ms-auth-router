from django.conf import settings


route_app_labels = {'contenttypes', 'sites', 'auth', 'admin', 'flatpages', 'redirects', 'auditlog', 'sessions'}


class DefaultRouter:
    try:
        token_table = settings.REST_AUTH_TOKEN_TABLE
    except (AttributeError, NameError):
        token_table = 'AUTHENTICATION_TOKEN'

    route_db_tables = {token_table, 'django_session'}

    try:
        auth_db = settings.AUTH_DB
    except (AttributeError, NameError):
        auth_db = 'default'

    if auth_db != 'default':
        auth_app_name = settings.AUTH_USER_MODEL.split('.')[0]
        route_app_labels.add(auth_app_name)

    def db_for_read(self, model, **hints):
        if hasattr(model, 'Database') and getattr(model.Database, 'db'):
            return getattr(model.Database, 'db')
        if model._meta.db_table in self.route_db_tables:
            return self.auth_db
        if model._meta.app_label in self.route_app_labels:
            return self.auth_db
        return None

    def db_for_write(self, model, **hints):
        if hasattr(model, 'Database') and getattr(model.Database, 'db'):
            return getattr(model.Database, 'db')
        if model._meta.db_table in self.route_db_tables:
            return self.auth_db
        if model._meta.app_label in self.route_app_labels:
            return self.auth_db
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels or
                obj1._meta.db_table in self.route_db_tables or
                obj2._meta.db_table in self.route_db_tables
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.auth_db
        return None
