from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from .helpers import template_to_out
import os

"""
Create recommended action layout:

/:app/actions/:resource/:action_id/

[app]
 |_ [actions]
    |_ [resource]
          |_

"""


class Command(BaseCommand):

    help = 'Configure defaul actions setup inside a module'

    def handle(self, *args, **options):

        # create directory structure
        # base_path = input('Path to the your module (e.g.: /code/:appname (no trailing slash): ')  # noqa: E501
        appname = input('The name of your django app: ')
        resource = input('Resource, e.g.: the name of the Django model class (e.g.: Todo): ')  # noqa: E501
        resource_url_path = input('The url path  to  your resource\'s base API. e.g. /todos/ (include leading and trailing slashes): ')  # noqa: E501

        context = {
            "resource": resource,
            # "code_path": base_path,
            "resource_path": resource_url_path,
            "appname": appname,
        }
        action_path = "{}/actions/{}".format(
            appname.lower(),
            resource.lower()
        )
        print(action_path)
        try:
            os.makedirs(action_path)
        except FileExistsError:
            print('actions folder already exists')
        except OSError as e:
            raise CommandError(e)

        Path(
            '{}/actions/__init__.py'.format(appname)
        ).touch()
        Path(
            '{}/actions/{}/__init__.py'.format(appname, resource)
        ).touch()

        # create registry:
        template_to_out(
            'djactions/action_registry.py',
            context,
            '{}/action_registry.py'.format(
                action_path
            )
        )

        # print instructions
        instructions = template_to_out('djactions/instructions.txt', context)
        print(instructions)
