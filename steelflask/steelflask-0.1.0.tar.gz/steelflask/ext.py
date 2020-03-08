import os
import shutil
from mako.template import Template

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class TemplateVariables:
    APP_NAME = 'app_name'
    VENV_FOLDER = 'venv_folder'


def copy_directory(src, dest, template_data={}, recursive=False):
    items = os.listdir(src)
    for item in items:
        item_src_path = os.path.join(src, item)
        item_dest_path = os.path.join(dest, item)
        if os.path.isdir(item_src_path):
            if recursive:
                os.makedirs(item_dest_path)
                copy_directory(item_src_path, item_dest_path)
        elif item.endswith('.mako'):
            template = Template(filename=item_src_path)
            output = template.render_unicode(**template_data).encode('utf-8', 'replace')
            with open(item_dest_path[:-5], "wb") as f:
                f.write(output)
        else:
            shutil.copy2(item_src_path, item_dest_path)
