# -*- coding:utf-8 -*-
from __future__ import division
from django_szuprefix.api.mixins import UserApiMixin
from django_szuprefix_saas.saas.mixins import PartyMixin
from . import models, serializers
from rest_framework import viewsets
from django_szuprefix.api.decorators import register


@register()
class TodoViewSet(PartyMixin, UserApiMixin, viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    filter_fields = ('user',)

