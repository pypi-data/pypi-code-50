#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A script to generate templates for Notable.

This script enables auto-generating Notable templates.

Example
-------
Getting help::


Section breaks are created with two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented:

Notes
-----
Add notes here.

"""

from PyInquirer import prompt
import re
import copy
import os
import json
import logging
from pathlib import Path
import pprint

from notate.note import Note
import notate.code_parser as code_parser
import notate.default_fields_generator as default_fields_generator
import notate.document_parser as document_parser
import notate.dotfile_manager as dotfile_manager
import notate.email_parser as email_parser
import notate.meeting_parser as meeting_parser
import notate.web_parser as web_parser
import notate.video_parser as video_parser


def setup_section_generators() -> dict:
    section_generators = dict()

    # Ordering based off importance
    section_generators["Meeting"] = meeting_parser.generate_meeting
    section_generators["Email"] = email_parser.generate_email
    section_generators["Document"] = document_parser.generate_document_note
    section_generators["Web Article"] = web_parser.generate_web_article_section
    section_generators["Video"] = video_parser.generate_video_section
    section_generators[
        "Open Questions"
    ] = default_fields_generator.generate_open_questions
    section_generators["Action Items"] = default_fields_generator.generate_action_items
    section_generators["Code"] = code_parser.generate_code
    section_generators["Table"] = default_fields_generator.generate_table
    section_generators[
        "Related Notes"
    ] = default_fields_generator.generate_related_notes
    section_generators["Diagram"] = default_fields_generator.generate_diagram
    section_generators["Math"] = default_fields_generator.generate_math

    logging.debug(f"Loaded section generators: {pprint.pformat(section_generators)}")

    return section_generators


def generate_sections(section_generators: dict, note):
    section_titles = []
    for generator_title in section_generators:
        section_titles.append({"name": generator_title})

    fields_to_generate = [
        {
            "type": "checkbox",
            "name": "fields_to_generate",
            "message": "Select optional fields to generate:",
            "choices": section_titles,
        }
    ]

    answers = prompt(fields_to_generate)

    logging.debug(
        f"User selected the following sections to generate: {pprint.pformat(answers)}"
    )

    for generator_title in answers["fields_to_generate"]:
        section_generators[generator_title](note)


def get_note_topic() -> str:
    questions = [
        {
            "type": "list",
            "name": "note_topic",
            "message": "Choose the high-level category of this note:",
            "choices": [
                "Meeting",
                "Programming",
                "Computing",
                "Fashion",
                "Fitness",
                "Finance",
                "Media",
                "Travel",
                "Cooking",
                "Gaming",
                "Car",
                "Home Improvement",
                "Career",
            ],
            "default": "Meeting",
        }
    ]

    answers = prompt(questions)
    logging.debug(f"note_topic: {answers['note_topic']}")
    return answers["note_topic"]


def setup_logger(outfile_name: str):
    format_string = (
        "%(levelname)s [ %(pathname)s:%(lineno)d %(funcName)s ] %(name)s - %(message)s"
    )

    import logging

    logging.basicConfig(
        filename=outfile_name, filemode="w", format=format_string, level=logging.DEBUG,
    )

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter(format_string)
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger("").addHandler(console)


def store_note(note):
    attach_subfolder = dotfile_manager.get_notable_attach_path()
    temp_subfolder = dotfile_manager.get_notable_temp_path()
    note.copy_attachments(attach_subfolder, temp_subfolder)

    notes_subfolder = dotfile_manager.get_notable_notes_path()
    note.write_note(notes_subfolder)


def create_note():
    section_generators = setup_section_generators()
    topic = get_note_topic()
    note = Note(topic)
    generate_sections(section_generators, note)
    return note


def take_note():
    dotfile_manager.setup_notable_folders()
    note = create_note()
    store_note(note)


if __name__ == "__main__":
    setup_logger("take_note.log")
    take_note()
