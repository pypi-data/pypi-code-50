#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import pendulum
import re
import logging
from PyInquirer import prompt
import os
import notate.utils as utils
import json


def prompt_for_title() -> str:
    questions = [
        {
            "type": "input",
            "name": "note_title",
            "message": "What is the title of this note?",
        }
    ]

    answers = prompt(questions)
    logging.debug(f"note_title: {answers['note_title']}")
    return answers["note_title"]


class Note(ABC):
    def __init__(self, topic: str):
        self.tags = set(["notable_script_template"])
        self.datetime_generated = pendulum.now("America/Los_Angeles")
        self.note_topic = topic
        self.chosen_title = ""
        self.metadata = dict()
        self.sections = dict()
        self.titles = dict()
        self.attachments = dict()

    def add_note_title_choice(
        self, section: str, subject: str, time=pendulum.now("America/Los_Angeles")
    ):
        assert (
            not self.chosen_title
        ), f"Title had already been chosen as {self.chosen_title} when you tried to overwrite with {subject}"

        date_string = time.format("YYYY-MM-DD")
        unsanitized_title = f"{self.note_topic} - {date_string} - {subject}"
        sanitized_title = utils.sanitize_string_as_path(unsanitized_title)

        if section in self.titles:
            self.titles[section].append(sanitized_title)
        else:
            self.titles[section] = [sanitized_title]

    def add_attachment(self, attachment_path: str):
        attachment_filename = os.path.basename(attachment_path)

        assert os.path.exists(
            attachment_path
        ), f"Could not locate attachment: {attachment_path}"
        self.attachments[attachment_filename] = {"original_path": attachment_path}

    def get_note_title(self) -> str:
        if self.chosen_title:
            logging.debug(
                f"User had already chosen title. Returning: {self.chosen_title}"
            )
            return self.chosen_title
        elif len(self.titles.keys()) == 0:
            logging.debug(f"No valid titles found. Prompting user...")
            self.chosen_title = prompt_for_title()
            return self.chosen_title
        else:
            logging.debug(f"Multiple valid titles. Prompting user to select.")
            title_choices = []
            for field, field_titles in self.titles.items():
                for title in field_titles:
                    title_choices.append(title)

            which_title = [
                {
                    "type": "list",
                    "name": "title_choice",
                    "message": f"Which title would you like?",
                    "choices": title_choices + ["None of these"],
                }
            ]
            answers = prompt(which_title)

            if answers["title_choice"] == "None of these":
                self.chosen_title = get_note_title()
            else:
                self.chosen_title = answers["title_choice"]

            return self.chosen_title

    def get_notable_header(self) -> str:
        tag_string = ""
        for tag in self.tags:
            if tag_string == "":
                tag_string = f"{tag}"
            else:
                tag_string += f", {tag}"

        time_string = self.datetime_generated.format("YYYY-MM-DD[T]HH:MM::SS.SSS[Z]")

        note_header = f"""---
tags: [{tag_string}]
title: '{self.get_note_title()}'
created: '{time_string}Z'
modified: '{time_string}Z'
---
# {self.get_note_title()}
"""

        logging.debug(f"Generated notable header as {note_header}")
        return note_header

    def add_tags(self, tags: list):
        for tag in tags:
            self.tags.add(tag)

    def add_metadata(self, field_type: str, metadata: dict):
        if field_type in self.metadata:
            self.metadata[field_type] = utils.dict_merge(
                self.metadata[field_type], metadata
            )
        else:
            self.metadata[field_type] = metadata

    def add_section(
        self, field_type: str, section_str: str, tags: list = [], metadata: dict = {}
    ):
        if field_type in self.sections:
            self.sections[field_type] += "\n" + section_str
        else:
            self.sections[field_type] = section_str
        if metadata:
            self.add_metadata(field_type, metadata)
        if tags:
            self.add_tags(tags)

    def get_note_string(self) -> str:
        attachment_section = ""

        # Add attachment metadata + data
        if self.attachments:
            attachment_section = "## Attachments\n"
            for attachment_filename in self.attachments.keys():
                attachment_section += (
                    f"[](@attachment/{self.get_note_title()}/{attachment_filename})\n"
                )
            self.metadata["Attachments"] = self.attachments

        metadata = json.dumps(
            self.metadata, indent=4, sort_keys=True, default=str
        )  # Default serializer needed to handle datetimes

        sections = ""
        for section_name, section_str in self.sections.items():
            logging.debug(
                f"Adding section: {section_name} to final note: {section_str}"
            )
            sections += f"## {section_name}\n"
            sections += section_str

        note_string = f"""{self.get_notable_header()}
{sections}
"""
        if attachment_section:
            note_string += attachment_section

        if metadata:
            note_string += f"""
## Metadata
```json
{metadata}
```
"""
        return note_string

    def copy_attachments(self, attach_subfolder: str, temp_subfolder: str = None):
        import shutil

        assert os.path.exists(
            attach_subfolder
        ), f"Attachment subfolder did not exist: {attach_subfolder}"

        # Attachments first so paths can be included in the final note.
        note_attach_dir = os.path.join(attach_subfolder, self.get_note_title())
        if not os.path.exists(note_attach_dir):
            os.mkdir(note_attach_dir)

        moved_attachments = []
        for attachment_name, attachment_traits in self.attachments.items():
            attachment_original_path = attachment_traits["original_path"]
            file_path = os.path.join(note_attach_dir, attachment_name)

            shutil.copy2(attachment_original_path, file_path)

            if temp_subfolder:
                if (
                    temp_subfolder in attachment_original_path
                ):  # This was a temporary file
                    os.remove(attachment_original_path)

            attachment_traits["final_path"] = file_path

    def write_note(self, notes_subfolder: str):
        note_path = os.path.join(notes_subfolder, f"{self.get_note_title()}.md")
        assert not os.path.exists(
            note_path
        ), f"A note with that same name already exists"
        with open(note_path, "w") as fh:
            fh.write(self.get_note_string())
