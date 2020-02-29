import factory
import hashlib
from .models import CodeFragment
from django.db.models.signals import post_save

@factory.django.mute_signals(post_save)
class EditorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CodeFragment

    # Please refer to Factory boy documentation
    # https://factoryboy.readthedocs.io
