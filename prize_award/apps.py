from django.apps import AppConfig


class PrizeAwardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prize_award'


    def ready(self) -> None:
        import prize_award.signals.handlers
