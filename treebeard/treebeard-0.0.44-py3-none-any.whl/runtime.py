from treebeard.helper import get_run_path, get_treebeard_config, TreebeardConfig
from google.cloud import storage  # type: ignore
import papermill as pm  # type: ignore
import threading
from datetime import datetime
import os
from typing import Any, Callable

storage_client: Any = storage.Client()
treebeard_config = get_treebeard_config() or TreebeardConfig()
bucket_name = "treebeard-notebook-outputs"
output_notebook_local_path = "/tmp/out.ipynb"
run_path = get_run_path()
global cancelled
cancelled = False


def log(message: str):
    print(f'{datetime.now().strftime("%H:%M:%S")}: {message}')


def set_interval(func: Callable, sec: int):
    def func_wrapper():
        if cancelled:
            return
        func()
        set_interval(func, sec)

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def cancel_interval():
    log("Cancelling Interval")
    global cancelled
    cancelled = True


def save_artifacts():
    log(f"saving all artifacts")

    notebook_upload_path = f"{run_path}/out.ipynb"
    if os.path.exists(output_notebook_local_path):
        log(f"Saving {output_notebook_local_path} to {notebook_upload_path}")
        notebook_blob = storage_client.bucket(bucket_name).blob(notebook_upload_path)
        notebook_blob.upload_from_filename("/tmp/out.ipynb")
    else:
        log("No output notebook to save")

    for output_dir in treebeard_config.output_dirs:
        for root, _, files in os.walk(output_dir, topdown=False):
            for name in files:
                prefix = "./"
                full_name = os.path.join(root, name)
                upload_path = f"{run_path}/{full_name[len(prefix):]}"
                log(f"Saving {full_name} to {upload_path}")
                blob = storage_client.bucket(bucket_name).blob(upload_path)
                blob.upload_from_filename(full_name)


def run():
    for output_dir in treebeard_config.output_dirs:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    set_interval(save_artifacts, 10)
    try:
        path, notebook_name = os.path.split(treebeard_config.notebook)
        log(f"Executing Notebook {notebook_name} in {path}")
        if len(path) > 0:
            os.chdir(path)
        pm.execute_notebook(
            notebook_name,
            output_notebook_local_path,
            progress_bar=False,
            request_save_on_cell_execute=True,
            autosave_cell_every=10,
            kernel_name="python3",
            log_output=True,
        )
    finally:
        cancel_interval()
        save_artifacts()
        log("Finished")


if __name__ == "__main__":
    run()
