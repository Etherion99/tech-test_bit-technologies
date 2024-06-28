from django.apps import AppConfig


class RealStateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'real_state'

    def ready(self):
        import real_state.signals
