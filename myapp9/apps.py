from django.apps import AppConfig


class Myapp9Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp9'

    def ready(self):
        import myapp9.signals


