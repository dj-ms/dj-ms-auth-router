from django.apps import AppConfig


class MsAuthRouterConfig(AppConfig):

    name = 'ms_auth_router'

    def ready(self):
        from django.apps import apps
        from .routers import route_app_labels
        all_apps = apps.get_app_configs()
        apps_for_route = list(app.name.split('.')[-1] for app in all_apps
                              if app.name.split('.')[-1] not in route_app_labels)

        def get_all_models():
            for app in apps_for_route:
                yield from apps.get_app_config(app).get_models()

        models = get_all_models()
        import logging
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.auth.models import Permission
        for model in models:
            try:
                content_type = ContentType.objects.get_for_model(model)
            except Exception as e:
                logging.error(f'Error while loading model {model}: {e}')
                continue
            else:
                meta = model._meta
                default_permissions = meta.default_permissions
                for permission in default_permissions:
                    Permission.objects.get_or_create(
                        codename=f'{permission}_{content_type.model}',
                        content_type=content_type,
                        defaults={'name': f'Can {permission} {content_type.name}'}
                    )
                extra_permissions = meta.permissions
                for permission in extra_permissions:
                    Permission.objects.get_or_create(
                        codename=permission[0],
                        content_type=content_type,
                        defaults={'name': permission[1]}
                    )

