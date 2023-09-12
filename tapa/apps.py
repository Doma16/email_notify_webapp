from django.apps import AppConfig


class TapaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tapa"

    def ready(self):
        from send_mail import start
        start.start()
