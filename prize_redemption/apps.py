from django.apps import AppConfig


class PrizeRedemptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prize_redemption'

    def ready(self) -> None:
        import prize_redemption.signals.handlers
