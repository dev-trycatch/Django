from django.apps import AppConfig


class Myapp7Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp7'

    def ready(self):
        import myapp7.signals
