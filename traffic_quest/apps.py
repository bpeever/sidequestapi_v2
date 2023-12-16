from django.apps import AppConfig


class TrafficQuestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traffic_quest'

    def ready(self):
        import traffic_quest.signals