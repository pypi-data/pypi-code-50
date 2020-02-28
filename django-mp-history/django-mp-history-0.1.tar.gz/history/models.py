
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class HistoryGroup(models.Model):

    name = models.CharField(_('Name'), max_length=255)

    code = models.CharField(_('Code'), max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('History group')
        verbose_name_plural = _('History groups')


class HistoryRecord(models.Model):

    ACTION_CREATE = 'creation'
    ACTION_CHANGE = 'change'
    ACTION_DELETE = 'deletion'

    ACTIONS = [
        ACTION_CREATE,
        ACTION_CHANGE,
        ACTION_DELETE
    ]

    ACTION_MESSAGES = {
        ACTION_CREATE: _('created'),
        ACTION_CHANGE: _('changed'),
        ACTION_DELETE: _('deleted')
    }

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='history_records',
        on_delete=models.CASCADE)

    text = models.TextField(
        _('Text'),
        max_length=1000)

    group = models.ForeignKey(
        HistoryGroup,
        verbose_name=_('Group'),
        on_delete=models.CASCADE)

    created = models.DateTimeField(
        _('Creation date'),
        auto_now_add=True)

    def __str__(self):
        return str(self.created)

    @classmethod
    def log_action(cls, action, group, user, obj, fields=None):

        meta = obj._meta

        if fields is None:
            fields = [f.name for f in meta.get_fields()]
            fields.remove('id')

        if not fields:
            return

        text = '{} #{} {}'.format(
            meta.verbose_name,
            obj.id,
            cls.ACTION_MESSAGES.get(action, action))

        for field in fields:

            try:
                if meta.get_field(field).choices:
                    value = getattr(obj, 'get_{}_display'.format(field))()
                else:
                    value = str(getattr(obj, field, '') or '---')

                text += '<br /> {}: {}'.format(
                    meta.get_field(field).verbose_name,
                    value)
            except Exception:
                pass

        try:
            group_obj = HistoryGroup.objects.get(code=group)
        except HistoryGroup.DoesNotExist:
            group_obj = HistoryGroup.objects.create(
                name=group.title(), code=group)

        return cls.objects.create(
            user=user,
            group=group_obj,
            text=text)

    class Meta:
        verbose_name = _('History record')
        verbose_name_plural = _('History records')
