from django import forms
from django.conf import settings

# resource actionform provides deault functionality for this resource:
# from example_app.actions.mixins import TodoActionFormMixin
from actions.forms.mixins import ActionFormMixin
from actions.fields import CommaSeparatedCharField

class {{action_camel_case}}Form(ActionFormMixin, forms.Form):
    """
    action_id: {{action_id}}
    """
    action_id = '{{resource|lower}}:{{action_id}}'
    # fields go here:
    # ...
    def get_object(self, pk):
        # return {{resource}}.objects.get(pk=pk)
        pass

    def get_stream_message(self, instance):
        return 'performed {{action_id}} on {}'.format(
            instance.pk
        )

    def save(self, request, pk=None):

        {{resource|lower}} = self.get_object(pk)
        # self.verify_has_permissions(request.user, [{{resource|lower}}])

        # Implement your action here
        # ..

        # self.perform_post_process(request, {{resource|lower}})
        # extra info to send back to the client, e.g.: count, batch_id etc
        meta = {}
        return (meta, {{resource|lower}})