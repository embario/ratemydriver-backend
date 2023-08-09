from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ratemydriver'

    def ready(self):
        import ratemydriver.signals  # noqa: F401
