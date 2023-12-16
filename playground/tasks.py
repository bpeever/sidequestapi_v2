from celery import shared_task
from time import sleep


@shared_task
def fake_celery_task():
    sleep(5)
    print("fake celery task ran successfully!")
    pass