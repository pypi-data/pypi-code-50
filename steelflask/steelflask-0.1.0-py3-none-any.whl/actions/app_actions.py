import os
import logging
from steelflask.ext import BASE_DIR, TemplateVariables, copy_directory


def generate_app(name, basic=False, venv_folder='venv'):
    """Generates a new app in current directory"""
    app_name_lowercase = name.lower()

    ensure_destination(app_name_lowercase)
    ensure_destination('tests')

    template_path = os.path.join(BASE_DIR, 'templates', 'basicapp') if basic else os.path.join(BASE_DIR, 'templates', 'flaskapp')

    template_data = {
        TemplateVariables.APP_NAME: app_name_lowercase,
        TemplateVariables.VENV_FOLDER: venv_folder
    }

    copy_directory(template_path, os.getcwd(), template_data)

    copy_directory(
        os.path.join(template_path, 'steelflaskapp'),
        os.path.join(os.getcwd(), app_name_lowercase),
        template_data)

    copy_directory(
        os.path.join(template_path, 'tests'),
        os.path.join(os.getcwd(), 'tests'),
        template_data)


def ensure_destination(name):
    dest = os.path.join(os.getcwd(), name)
    if os.path.isdir(dest) and os.listdir(dest):
        logging.error(f"A directory with name {name} is already exists and not empty.")
        exit()
    else:
        os.makedirs(dest, exist_ok=True)
