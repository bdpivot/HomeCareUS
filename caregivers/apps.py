from django.apps import AppConfig


class CaregiversConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'caregivers'
    verbose_name = 'Caregivers Management'

    def ready(self):
        try:
            import caregivers.signals  # noqa
        except ImportError:
            pass
