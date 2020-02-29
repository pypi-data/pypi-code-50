import factory
import hashlib
from .models import Like
from django.db.models.signals import post_save

@factory.django.mute_signals(post_save)
class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like

    # Please refer to Factory boy documentation
    # https://factoryboy.readthedocs.io
