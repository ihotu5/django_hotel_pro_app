from django.apps import AppConfig


class SecondHotelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'second_hotel'

    def ready(self):
        import second_hotel.signals
