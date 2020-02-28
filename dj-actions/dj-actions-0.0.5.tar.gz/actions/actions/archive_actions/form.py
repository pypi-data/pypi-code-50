from django import forms
from django.conf import settings
from rest_framework import exceptions
# resource actionform provides deault functionality for this resource:
# from example_app.actions.mixins import TodoActionFormMixin
from actions.forms.mixins import ActionFormMixin
from actions.models import ActionEvent


class ArchiveActionsForm(ActionFormMixin, forms.Form):
    """
    action_id: archive_actions
    """
    action_id = 'actionevent:archive_actions'
    delete_before = forms.DateTimeField(required=True)
    # fields go here:
    # ...
    def get_object(self, pk):
        # return ActionEvent.objects.get(pk=pk)
        pass

    def get_stream_message(self, instance):
        return 'performed archive_actions on {}'.format(
            instance.pk
        )

    def save(self, request, pk=None):
        if not request.user.is_superuser:
            raise exceptions.PermissionDenied('Permission denied.')
        delete_before = self.cleaned_data.get('delete_before')
        expired = ActionEvent.objects.filter(created_date__lte=delete_before)
        expired.delete()

        meta = {
            "count": expired.count()
        }
        return (meta, expired)