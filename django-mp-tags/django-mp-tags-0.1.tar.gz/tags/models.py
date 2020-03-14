
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from model_search import model_search


class TagGroupManager(models.Manager):

    def get_queryset(self):
        return TagGroupQuerySet(self.model, using=self._db)

    def find(self, query):
        return self.get_queryset().find(query)


class TagGroupQuerySet(models.QuerySet):

    def find(self, query):
        tag_fields = ['text_' + c for c, n in settings.LANGUAGES]
        tags = model_search(query, Tag.objects.all(), tag_fields)
        return self.filter(tags__in=tags)


class TagGroup(models.Model):

    name = models.CharField(_('Text'), max_length=255, unique=True)

    objects = TagGroupManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Tag group')
        verbose_name_plural = _('Tag groups')


class Tag(models.Model):

    group = models.ForeignKey(
        TagGroup,
        verbose_name=_('Group'),
        on_delete=models.SET_NULL,
        related_name='tags',
        null=True,
        blank=True)

    text = models.CharField(_('Text'), max_length=255, db_index=True)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ('group', 'text', )
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class TagGroupsField(models.ManyToManyField):

    def __init__(
            self,
            to=TagGroup,
            verbose_name=_("Tag groups"),
            blank=True,
            *args,
            **kwargs):
        super().__init__(
            to=to,
            verbose_name=verbose_name,
            blank=blank,
            *args,
            **kwargs)
