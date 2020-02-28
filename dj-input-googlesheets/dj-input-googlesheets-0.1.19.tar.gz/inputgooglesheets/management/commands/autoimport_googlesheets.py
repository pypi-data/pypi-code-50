from django.core.management.base import BaseCommand, CommandError
from ...utils import Utils


class Command(BaseCommand):
    help = 'Periodically import autoimportable google spreadsheets.'

    def handle(self, *args, **options):
        Utils.autoimport_forever()
