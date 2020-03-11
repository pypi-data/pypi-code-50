import os
import shutil
from typing import List

import forge_template.util.log_utils as utils
from forge_template.handler.handler import BaseHandler
from forge_template.util.paths import (
    DATABRICKS_SCRIPT_NAME,
    DATABRICKS_WORKFLOW_TEMPLATE_NAME,
    POWERBI_SCRIPT_NAME,
    POWERBI_WORKFLOW_TEMPLATE_NAME,
    SCRIPT_TEMPLATE_FOLDER,
    WORKFLOW_TEMPLATE_FOLDER,
)
from forge_template.util.yaml_util import DATABRICKS_CONFIG_NAME, POWERBI_CONFIG_NAME

SCRIPT_FOLDER = "pipeline_scripts"
WORKFLOW_ACTION_FOLDER = os.path.join(".github", "workflows")
GITHUB_ACTION_HANDLER_NAME = "github_actions"


class GithubActionsHandler(BaseHandler):
    def __init__(self, tool_name: str) -> None:
        self._tool = tool_name
        self._paths_to_create = [WORKFLOW_ACTION_FOLDER, SCRIPT_FOLDER]

        if tool_name == DATABRICKS_CONFIG_NAME:
            self._script_to_add = os.path.join(SCRIPT_FOLDER, DATABRICKS_SCRIPT_NAME)
            self._template_to_add = os.path.join(WORKFLOW_ACTION_FOLDER, DATABRICKS_WORKFLOW_TEMPLATE_NAME)
        elif tool_name == POWERBI_CONFIG_NAME:
            self._script_to_add = os.path.join(SCRIPT_FOLDER, POWERBI_SCRIPT_NAME)
            self._template_to_add = os.path.join(WORKFLOW_ACTION_FOLDER, POWERBI_WORKFLOW_TEMPLATE_NAME)
        else:
            raise RuntimeError(
                f"Unexpected tool. Got {self._tool}, but expected one of "
                f"{[POWERBI_CONFIG_NAME, DATABRICKS_CONFIG_NAME]}"
            )

        self._to_from_paths = [
            (self._script_to_add, os.path.join(SCRIPT_TEMPLATE_FOLDER, os.path.basename(self._script_to_add))),
            (self._template_to_add, os.path.join(WORKFLOW_TEMPLATE_FOLDER, os.path.basename(self._template_to_add))),
        ]

        self._created_folders: List[str] = []
        self._copied_files: List[str] = []

        super().__init__(name=GITHUB_ACTION_HANDLER_NAME, config={})

    def create_preview(self) -> None:
        pass

    def print_preview(self) -> None:
        utils.print_resource_to_add(self._paths_to_create, "Directory")
        utils.print_resource_to_add(
            [self._script_to_add, self._template_to_add], "File",
        )

    def setup(self) -> None:
        self.__create_path()
        self.__copy_files()

    def rollback(self) -> None:
        if self._copied_files:
            utils.print_rollback("Files")
            for file in self._copied_files:
                self.__delete_path(file)

        if self._created_folders:
            utils.print_rollback("Folders")
            for folder in self._created_folders:
                self.__delete_path(folder)

    def delete_all_resources(self):
        for path in self._paths_to_create:
            self.__delete_path(path)

    @staticmethod
    def __delete_path(path: str) -> None:
        if os.path.exists(path):
            if os.path.isdir(path):
                os.rmdir(path)
                utils.print_success_deleted(path, "Directory")
            else:
                os.remove(path)
                utils.print_success_deleted(path, "File")

    def __create_path(self) -> None:
        for path in self._paths_to_create:
            if not os.path.exists(path):
                os.makedirs(path)
                self._created_folders.append(path)
                utils.print_success_created(path, "Directory")

    def __copy_files(self) -> None:
        for (to_path, from_path) in self._to_from_paths:
            shutil.copyfile(from_path, to_path)
            self._copied_files.append(to_path)
            file_name = os.path.basename(to_path)
            folder_name = os.path.dirname(to_path)
            utils.print_success_added(folder_name, "Directory", file_name, "File")

    @property
    def created_folders(self):
        return self._created_folders
