from django import forms
from django.conf import settings

# resource actionform provides deault functionality for this resource:
# from example_app.actions.mixins import TodoActionFormMixin
from actions.forms.mixins import ActionFormMixin
from actions.fields import CommaSeparatedCharField

class MarkDoneForm(ActionFormMixin, forms.Form):
    """
    action_id: mark_done
    """
    action_id = 'todo:mark_done'
    # fields go here:
    # ...
    def get_object(self, pk):
        # return Todo.objects.get(pk=pk)
        pass

    def get_stream_message(self, instance):
        return 'performed mark_done on {}'.format(
            instance.pk
        )

    def save(self, request, pk=None):

        todo = self.get_object(pk)
        # self.verify_has_permissions(request.user, [todo])

        # Implement your action here
        # ..

        # self.perform_post_process(request, todo)
        # extra info to send back to the client, e.g.: count, batch_id etc
        meta = {}
        return (meta, todo)