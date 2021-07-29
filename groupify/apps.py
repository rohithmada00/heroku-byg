from django.apps import AppConfig


class GroupifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groupify'
    def ready(self):
        import groupify.signals
