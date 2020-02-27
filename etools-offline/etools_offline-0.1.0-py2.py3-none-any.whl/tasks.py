import os

import requests
from django.conf import settings
from unicef_attachments.models import Attachment, FileType, generate_file_path

from etools_offline.utils import get_task_app

app = get_task_app()


@app.task
def move_file(obj, code, url):
    """Move data storage to app storage"""
    attachment = Attachment.objects.create(
        content_object=obj,
        code=code,
        file_type=FileType.objects.get(code=code),
    )
    filename = os.path.join(
        settings.MEDIA_ROOT,
        generate_file_path(attachment, url.split('/')[-1])
    )

    # How does this impact azure storage setups?
    try:
        os.makedirs(os.path.dirname(filename))
    except FileExistsError:
        pass

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # filter out keep-alive new chunks
                if chunk:
                    f.write(chunk)
    attachment.file = filename
    attachment.save()
