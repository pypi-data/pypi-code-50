from PyInquirer import prompt
import notate.utils as utils
import os
import notate.dotfile_manager as dotfile_manager


def generate_web_article_section(note):
    while True:
        questions = [
            {
                "type": "input",
                "name": "title",
                "message": "What is the subject of this article/webpage?",
            },
            {
                "type": "input",
                "name": "url",
                "message": "What is the url of the webpage?",
            },
            {
                "type": "confirm",
                "name": "is_create_archive",
                "message": "Should this webpage be archived as an attachment?",
            },
        ]

        answers = prompt(questions)

        if answers["is_create_archive"]:
            # Directory to store downloaded items before the attachment fodler is created
            notable_temp_path = dotfile_manager.get_notable_temp_path()

            target_name = utils.sanitize_string_as_path(answers["title"]) + ".pdf"
            target_path = os.path.join(notable_temp_path, target_name)

            utils.save_webpage(answers["url"], target_path)
            note.add_attachment(target_path)

        metadata = {
            answers["title"]: {
                "title": answers["title"],
                "is_create_archive": answers["is_create_archive"],
                "url": answers["url"],
            }
        }

        note.add_note_title_choice("Web Article", answers["title"])
        note.add_metadata("Web Article", metadata=metadata)

        # Check if user wants to add more
        questions = [
            {
                "type": "confirm",
                "name": "another_webpage",
                "message": "Would you like to attach another webpage?",
            }
        ]
        is_another_webpage = prompt(questions)["another_webpage"]
        if not is_another_webpage:
            break

    note.add_tags(["Web Article"])
