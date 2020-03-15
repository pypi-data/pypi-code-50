from django.core.management.base import BaseCommand, CommandError
from newsboard import models
from newsboard import tasks


class Command(BaseCommand):
    help = "Update streams' posts"

    def add_arguments(self, parser):
        parser.add_argument('-n', '--non-auto', action='store_false')

    def handle(self, *args, **options):
        stream_ids = models.Stream.objects.values_list('id', flat=True)
        for id_ in stream_ids:
            tasks.update_stream(id_)
