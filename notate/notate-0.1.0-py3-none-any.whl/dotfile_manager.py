import os
from pathlib import Path
from PyInquirer import prompt
import logging


NOTABLE_FOLDER_PATH = None
NOTABLE_TEMP_PATH = None
NOTABLE_NOTES_PATH = None
NOTABLE_ATTACH_PATH = None


def setup_notable_folders():
    global NOTABLE_FOLDER_PATH
    global NOTABLE_TEMP_PATH
    global NOTABLE_NOTES_PATH
    global NOTABLE_ATTACH_PATH

    assert (
        NOTABLE_FOLDER_PATH is None
    ), f"NOTABLE_FOLDER_PATH was already set: {NOTABLE_FOLDER_PATH}"
    assert (
        NOTABLE_TEMP_PATH is None
    ), f"NOTABLE_TEMP_PATH was already set: {NOTABLE_TEMP_PATH}"
    assert (
        NOTABLE_NOTES_PATH is None
    ), f"NOTABLE_NOTES_PATH was already set: {NOTABLE_NOTES_PATH}"
    assert (
        NOTABLE_ATTACH_PATH is None
    ), f"NOTABLE_ATTACH_PATH was already set: {NOTABLE_ATTACH_PATH}"

    dotfile_path = os.path.join(Path.home(), ".notate")
    print(dotfile_path)

    assert os.path.exists(
        dotfile_path
    ), f"Dotfile (~/.notate) does not exist. Please create one."

    notable_data_directories = []
    with open(dotfile_path, "r") as fh:
        notable_data_directories = fh.readlines()
        notable_data_directories = [
            data_dir.strip() for data_dir in notable_data_directories
        ]

    logging.debug(
        f"Found the following notable directories from the dotfile: {notable_data_directories}"
    )

    questions = [
        {
            "type": "list",
            "name": "notable_folder",
            "message": "Which notable data directory should this note be saved in (parsed from ~/.notate)?",
            "choices": notable_data_directories,
        }
    ]

    answers = prompt(questions)
    notable_folder = answers["notable_folder"]
    assert os.path.exists(
        notable_folder
    ), f"Notable folder {notable_folder} does not exist."
    notable_note_subfolder = os.path.join(notable_folder, "notes")
    assert os.path.exists(
        notable_note_subfolder
    ), f"Notable sub-folder {notable_note_subfolder} does not exist."
    notable_attach_subfolder = os.path.join(notable_folder, "attachments")
    assert os.path.exists(
        notable_attach_subfolder
    ), f"Notable sub-folder {notable_attach_subfolder} does not exist."

    notable_temp_subfolder = os.path.join(notable_folder, "temp")
    if not os.path.exists(notable_temp_subfolder):
        os.mkdir(notable_temp_subfolder)

    logging.debug(f"notable_note_subfolder identified as: {notable_note_subfolder}")

    NOTABLE_FOLDER_PATH = notable_folder
    NOTABLE_TEMP_PATH = notable_temp_subfolder
    NOTABLE_NOTES_PATH = notable_note_subfolder
    NOTABLE_ATTACH_PATH = notable_attach_subfolder


def get_notable_folder_path():
    if not NOTABLE_FOLDER_PATH:
        setup_notable_folders()
    return NOTABLE_FOLDER_PATH


def get_notable_notes_path():
    if not NOTABLE_NOTES_PATH:
        setup_notable_folders()
    return NOTABLE_NOTES_PATH


def get_notable_attach_path():
    if not NOTABLE_ATTACH_PATH:
        setup_notable_folders()
    return NOTABLE_ATTACH_PATH


def get_notable_temp_path():
    if not NOTABLE_TEMP_PATH:
        setup_notable_folders()
    return NOTABLE_TEMP_PATH
