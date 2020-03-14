import os
import tempfile
import uuid
import json
from pathlib import Path
from PyQt5.QtCore import QRect, QMargins

CONFIG_ARCHIVE = "archive"
MARGIN = 5
# SUBWINDOW_ADJUST = 100
MAIN_WINDOW_SIZE = QRect(0,0,1200,800)
SUB_WINDOW_SIZE = QRect(0,0,1200,800)
QMARGIN = QMargins(MARGIN, MARGIN, MARGIN, MARGIN)
STEPS_ORDER = [
    'parking_image_input', 'parking_checker', 'notifier', 'metrics_collector' ,'archiver'
]

this_dir, this_filename = os.path.split(__file__)


new_job_template = {
    "id": "undefined",
    "name": 'unsaved new job',
    "priority": 0,
    "autostart": True,
    "routes": [
        {
            "name": "default_sequence",
            "type_name": "sequence",
            "steps": [
            ]
        }
    ],
    "required_workers": [

    ],
    "required_data_support": [
        {
            "name": "parking_detection_data",
            "content_type": "application/json"
        }
    ]
}


def local_job_dir( job_id ):
    jdir = os.path.join(tempfile.gettempdir(), job_id)
    if not os.path.exists(jdir):
        os.makedirs(jdir,exist_ok=True)
    return jdir

def local_img_name(job_id):
    return os.path.join( local_job_dir(job_id), track_uuid() + '.jpg' )


def get_job_step_configuration(job, job_step_type):
    if not job or not 'required_workers' in job:
        return None
    for wrk in job['required_workers']:
        if wrk['worker_type'] == job_step_type and 'configuration' in wrk:
            return wrk['configuration']
    return None

def get_job_step_configuration_value(job, job_step_type, conf_entry):
    conf = get_job_step_configuration(job,job_step_type)
    if conf and conf_entry in conf:
        return conf[conf_entry]
    else:
        return None

def track_uuid():
    return str(uuid.uuid1())


PARKING_DIR = '.parking-app'
SETTINGS = 'config.json'
GCLOUD_KEYFILE = 'gcloud.authkeyfile'

def _base_dir():
    basedir = os.path.join(str(Path.home()), PARKING_DIR)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    return basedir


def get_settings():
    basedir = _base_dir()
    if os.path.exists(os.path.join(basedir, SETTINGS)):
        with open(os.path.join(basedir, SETTINGS), 'r') as f:
            return json.load(f)
    return {}


def save_settings(settings):
    basedir = _base_dir()
    with open(os.path.join(basedir, SETTINGS), 'w') as f:
        json.dump(settings, f)


def get_key_file():
    sets = get_settings()
    if sets and GCLOUD_KEYFILE in sets:
        return sets[GCLOUD_KEYFILE]
    return None