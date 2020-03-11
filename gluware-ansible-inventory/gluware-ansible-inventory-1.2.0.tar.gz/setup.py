
import os.path
from setuptools import setup

# Read the README.md file to a variable to pass to setup.
CURDIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(CURDIR, "README.md")) as file_id:
    README = file_id.read()

setup(
    name = "gluware-ansible-inventory",
    version = "1.2.0",
    description = "Gluware Ansible Inventory",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://gluware.com",
    author = "Gluware Inc.",
    author_email = "support@gluware.com",
    data_files = [  ('/usr/share/ansible/plugins/inventory', ['inventory/glu_devices.py']),
                    ('/usr/share/ansible/plugins/modules', ['modules/glu_audit_config.py', 
                                'modules/glu_capture_config.py',
                                'modules/glu_run_discover_device_attributes.py',
                                'modules/glu_update_device_attributes.py'])],
)

