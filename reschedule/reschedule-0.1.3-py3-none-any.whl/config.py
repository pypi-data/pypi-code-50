from datetime import datetime
from pathlib import Path
import json
import sys
import os

# create the config files
config_directory=Path(os.path.join(str(Path.home()), '.cache/reschedule'))
_config_file=Path(os.path.join(str(config_directory), 'config.json'))
config_directory.mkdir(parents=True, exist_ok=True)
_config_file.touch(exist_ok=True)

# default configuration
_default_config = {
    'task_file_path': str(os.path.join(str(Path.home()), 'todos.md')),
    'task_calendar_name': 'Reschedule Tasks',
    'work_start_time': '08:00',
    'work_end_time': '18:00',
    'chunk_size': 15,
    'default_est': '30m'
}

# if the config file is empty write the default config
if os.stat(str(_config_file)).st_size == 0:
    _config_file.write_text(json.dumps(_default_config))

_user_config = json.loads(_config_file.read_text())

# the scopes the app uses
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar",
]

# Path to task file
task_file_path = _user_config['task_file_path']
if not os.path.exists(task_file_path):
    sys.exit('Task file ' + task_file_path + ' does not exist. Verify the correct path in ' + str(_config_file))

# the name of the task calendar in google. MUST BE UNIQUE
task_calendar_name = _user_config['task_calendar_name']

_start_time = datetime.strptime(_user_config['work_start_time'], '%H:%M')
# time that you start work every day
work_start_time = datetime.now().replace(hour=_start_time.hour, minute=_start_time.minute, second=0, microsecond=0)

_end_time = datetime.strptime(_user_config['work_end_time'], '%H:%M')
# time that you stop work every day
work_end_time = datetime.now().replace(hour=_end_time.hour, minute=_end_time.minute, second=0, microsecond=0)

# minimum event time in minutes
chunk_size = int(_user_config['chunk_size'])

default_est = _user_config['default_est']

developer_key= "AIzaSyBUHmDb5f6Mrt2IZIa_h0QfAp0Xqkgou4E"