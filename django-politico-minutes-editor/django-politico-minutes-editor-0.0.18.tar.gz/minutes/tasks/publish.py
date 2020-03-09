import requests

from celery import shared_task
from django.conf import settings
from minutes.models import Edition

headers = {
    "Authorization": "Token {}".format(settings.MINUTES_API_TOKEN),
    "Content-Type": "application/json",
}


@shared_task(acks_late=True)
def publish(edition):
    data = {"action": "publish", "data": edition}

    requests.post(settings.MINUTES_BAKERY_URL, json=data, headers=headers)


@shared_task(acks_late=True)
def unpublish(edition):
    data = {"action": "unpublish", "data": edition}

    e = Edition.objects.get(id=edition)
    e.live = False
    e.save()

    if e == Edition.objects.latest_live(e.vertical):
        publish_latest(e.vertical.id.hex)

    requests.post(settings.MINUTES_BAKERY_URL, json=data, headers=headers)


@shared_task(acks_late=True)
def publish_latest(vertical):
    publish(Edition.objects.latest_live(vertical).id.hex)


@shared_task(acks_late=True)
def publish_if_ready(edition):
    e = Edition.objects.get(id=edition)
    if e.should_publish():
        publish(edition)
