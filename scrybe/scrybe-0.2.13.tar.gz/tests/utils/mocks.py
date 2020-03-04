import functools
import os
import sys

from datetime import datetime


def send_uploads_to_file(folder='~/tmp/scrybe/upload_data', prevent_upload=True):
    folder_path = os.path.expanduser(folder)
    os.makedirs(folder_path, exist_ok=True)

    main_module = sys.modules['__main__']
    filename = getattr(main_module, '__file__', "interactive")
    _, filename = os.path.split(filename)
    filename = filename.replace('.py', '')
    filename = filename.replace('.ipynb', '')
    log_filename = "%s_%s.log" % (filename, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    log_filename = os.path.join(folder_path, log_filename)
    print("Sending upload packets to: %s" % log_filename)

    import scrybe.internal.uploader as uploader

    def send_data_wrapper(fn):
        @functools.wraps(fn)
        def wrapped_fn(self, json_data_list):
            import json
            if len(json_data_list) > 0:
                with open(log_filename, 'a') as log_file:
                    json.dump(json_data_list, log_file, indent=2)
            if not prevent_upload:
                fn(self, json_data_list)
        return wrapped_fn

    uploader.DataUploader._send_data = send_data_wrapper(uploader.DataUploader._send_data)
