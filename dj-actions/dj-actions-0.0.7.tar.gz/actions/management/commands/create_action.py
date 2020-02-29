from django.core.management.base import BaseCommand
from django.utils.module_loading import import_string
from pathlib import Path
from .helpers import (
    template_to_out,
    create_file_path
)
from actions.util import (
    STATUS,
    ACTION_TYPE,
)
import os


class Command(BaseCommand):

    help = 'Create a new action'

    def handle(self, *args, **options):

        # create directory structure
        # base_path = input('Path to the your module (e.g.: /code/:appname (no trailing slash): ')  # noqa: E501
        # base_path = "{}/actions".format(base_path)

        appname = input('The name of your django app: ')
        resource = input('Resource, e.g.: the name of the Django model class (e.g.: Todo): ')  # noqa: E501
        resource_url_path = input('The url path  to  your resource\'s base API. e.g. /todos/ (include leading and trailing slashes): ')  # noqa: E501
        action_id = input('The name of the action you are implementing (e.g.: make_done or start): ')  # noqa: E501
        action_type = input('Is this a bulk (e.g.: operation can be performed againstt multiple instances) or an innstance (e.g.: it is performed against a single instance) type of action? [bulk/instance]: ')  # noqa: E501

        # /:app/actions/:resource/:action_id/
        base_path = "{}/actions/{}/{}/".format(
            appname.lower(),
            resource.lower(),
            action_id.lower()
        )
        action_import_path = "{}.actions.{}.{}".format(
            appname,
            resource.lower(),
            action_id
        )
        action_camel_case = ('').join([word[0].upper() + word[1:] for word in action_id.split('_')])  # noqa: E501
        context = {
            "resource": resource,
            "code_path": base_path,
            "resource_path": resource_url_path,
            "appname": appname,
            'action_id': action_id,
            'action_camel_case': action_camel_case,
            'action_import_path': action_import_path,
            'action_type': action_type,
        }
        confirmation = template_to_out('djactions/create_action_confirmation.txt', context)
        print(confirmation)
        confirm = input('Continue? Type y to continue, any other key to exit [y]  ')
        if confirm:
            action_base_path = base_path
            test_path = action_base_path + '/tests/'
            create_file_path(test_path)

            # create __init__ files:
            Path(
                '{}__init__.py'.format(action_base_path)
            ).touch()
            Path(
                '{}__init__.py'.format(test_path)
            ).touch()

            template_to_out(
                'djactions/test_form.py',
                context,
                '{}/{}'.format(test_path, 'test_form.py')
            )
            template_to_out(
                'djactions/test_api.py',
                context,
                '{}/{}'.format(test_path, 'test_api.py')
            )
            template_to_out(
                'djactions/form.py',
                context,
                '{}/{}'.format(action_base_path, 'form.py')
            )
            template_to_out(
                'djactions/definition.yaml',
                context,
                '{}/{}'.format(action_base_path, 'definition.yaml')
            )
            template_to_out(
                'djactions/README.md',
                context,
                '{}/{}'.format(action_base_path, 'README.md')
            )

            # UPDATE ACTIOIN_REGISTRY
            # example_app.actions.todo.action_registry.action_list
            existing_apps = import_string(
                "{}.actions.{}.action_registry.action_list".format(
                    appname,
                    resource.lower()
                )
            )
            existing_apps.append((action_id, action_type, STATUS.ALPHA.value))
            context.update({
                "action_list": existing_apps
            })
            reg_path = "{}/actions/{}/".format(
                appname.lower(),
                resource.lower()
            )
            template_to_out(
                'djactions/action_registry.py',
                context,
                '{}/{}'.format(
                    reg_path,
                    'action_registry.py'
                )
            )

            # print success
            success_notes = template_to_out(
                'djactions/create_action_success.txt',
                context
            )
            print(success_notes)
        else:
            print('cancelled')
