from django.core.management.base import BaseCommand, CommandError
import os
from .helpers import template_to_out

class Command(BaseCommand):

    help = 'Configure defaul actions setup inside a module'

    def handle(self, *args, **options):

        # create directory structure
        base_path = input('Path to the your module (e.g.: /code/:appname (no trailing slash): ')  # noqa: E501
        resource = input('Resource, e.g.: the name of the Django model class (e.g.: Todo): ')  # noqa: E501
        resource_url_path = input('The url path  to  your resource\'s base API. e.g. /todos/ (include leading and trailing slashes): ')  # noqa: E501
        appname = input('The name of your django app: ')

        context = {
            "resource": resource,
            "code_path": base_path,
            "resource_path": resource_url_path,
            "appname": appname,
        }

        try:
            os.makedirs(base_path)
        except FileExistsError:
            print('actions folder already exists')
        except OSError as e:
            raise CommandError(e)

        # create registry:
        template_to_out(
            'djactions/action_registry.py',
            context,
            '{}action_registry.py'.format(base_path)
        )

        # print instructions
        instructions = template_to_out('djactions/instructions.txt', context)
        print(instructions)
