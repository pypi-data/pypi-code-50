from datetime import datetime

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar",
]

# Path to task file
task_file_path = "/Users/lukemurray/Dropbox/todo.md"

# the name of the task calendar in google. MUST BE UNIQUE
task_calendar_name = "Markdown Tasks"

# time that you start work every day
work_start_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

# time that you stop work every day
work_end_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

# minimum event time in minutes
chunk_size = 15
