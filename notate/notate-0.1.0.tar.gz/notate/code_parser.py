from PyInquirer import prompt
import os
import re
import logging


def generate_code(note):
    while True:
        questions = [
            {
                "type": "list",
                "name": "language",
                "message": "What langauge is this code in?",
                "choices": [
                    "Lua",
                    "Python",
                    "C++",
                    "Rust",
                    "CMake",
                    "Bash",
                    "Make",
                    "Shell",
                    "Markdown",
                    "Other",
                ],
            },
            {
                "type": "list",
                "name": "type",
                "message": "What aspect of code are you notating?",
                "choices": [
                    "Bug",
                    "Design Pattern",
                    "Error Signature",
                    "Syntax",
                    "Library",
                    "Process",
                ],
            },
            {
                "type": "input",
                "name": "title",
                "message": "What is this code solving/about?",
            },
        ]

        answers = prompt(questions)

        metadata = {
            answers["title"]: {
                "language": answers["language"],
                "title": answers["title"],
                "type": answers["type"],
            }
        }

        subject = f"{answers['type']} - {answers['title']}"
        note.add_note_title_choice("Code", subject)

        code_string = f"""
### {answers['title']}
```{answers['language']}

```
"""

        note.add_section(
            "Code", code_string, metadata=metadata, tags=["Code", answers["language"]]
        )

        # Check if user wants to add more
        questions = [
            {
                "type": "confirm",
                "name": "another_code",
                "message": "Would you like to create another code section?",
            }
        ]
        is_another_code = prompt(questions)["another_code"]
        if not is_another_code:
            break
