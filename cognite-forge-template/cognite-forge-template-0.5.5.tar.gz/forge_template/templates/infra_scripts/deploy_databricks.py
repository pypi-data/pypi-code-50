import base64
import os
import sys
from collections import deque

from databricks_api import DatabricksAPI
from ruamel.yaml import YAML

CONFIG_FILE_PATH = "config.yaml"

with open(CONFIG_FILE_PATH) as f:
    config = YAML(typ="safe").load(f)["databricks"]

if len(sys.argv) < 2:
    raise RuntimeError("Expected Databricks token to passed as a command line argument.")

else:
    handler = DatabricksAPI(host=config["host"], token=sys.argv[1])
    prod_workspace = config["production"]["workspace_path"]
    stack = deque(["databricks"])
    local_paths = []
    while stack:
        curr_path = stack.pop()
        if os.path.isfile(curr_path):
            local_paths.append(curr_path)
        else:
            sub_paths = list(map(lambda p: os.path.join(curr_path, p), os.listdir(curr_path)))
            stack.extend(sub_paths)

    upload_paths = list(map(lambda p: p.replace("databricks", prod_workspace), local_paths))
    upload_dirs = set(map(lambda p: os.path.dirname(p).replace("databricks", prod_workspace), local_paths))

    print("\nDelete production workspace ...")
    handler.workspace.delete(prod_workspace, recursive=True)
    print("Done deleting production workspace")

    print("\nCreating directories in production workspace ...")
    for d in upload_dirs:
        handler.workspace.mkdirs(d)
        print(f"Created {d}")
    print("Done creating directories")

    print("\nUploading notebooks ...")
    for local_path, upload_path in zip(local_paths, upload_paths):
        with open(local_path, "rb") as f:
            content = f.read()
            encoded_content = base64.b64encode(content).decode()
            handler.workspace.import_workspace(upload_path, language="PYTHON", format="SOURCE", content=encoded_content)
            print(f"Uploaded {local_path} as {upload_path}")
    print("Done uploading notebooks")
