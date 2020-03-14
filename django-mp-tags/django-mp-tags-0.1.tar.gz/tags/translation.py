
from modeltranslation.translator import translator

from tags.models import Tag


translator.register(Tag, fields=['text'])
