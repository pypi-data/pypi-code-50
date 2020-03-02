from PyInquirer import prompt
import notate.utils as utils
import notate.dotfile_manager as dotfile_manager


def generate_document_note(note):
    while True:
        questions = [
            {
                "type": "input",
                "name": "document_name",
                "message": "What is this document's name?",
            },
            {
                "type": "list",
                "name": "document_location",
                "message": "Where is this document located?",
                "choices": ["url", "local"],
            },
            {
                "type": "confirm",
                "name": "is_create_archive",
                "message": "Should this document be archived as an attachment?",
            },
        ]

        answers = prompt(questions)

        if answers["is_create_archive"]:
            if answers["document_location"] == "url":
                questions = [
                    {
                        "type": "input",
                        "name": "url",
                        "message": "What is the URL of this document? (Note: it should be a downloadable format such as .pdf)",
                    }
                ]
                url = prompt(questions)["url"].strip()
                # Remove '' introduced by terminal due to spaces
                if url.startswith("'"):
                    url = url[1:]
                if url.endswith("'"):
                    url = url[:-1]

                path_to_original = url  # For metadata

                # Directory to store downloaded items before the attachment fodler is created
                notable_temp_path = dotfile_manager.get_notable_temp_path()
                temp_attach_path = utils.download_file(url, notable_temp_path)
                note.add_attachment(temp_attach_path)
            elif answers["document_location"] == "local":
                questions = [
                    {
                        "type": "input",
                        "name": "local_path",
                        "message": "What is the local path of this document?",
                    }
                ]
                local_doc_path = prompt(questions)["local_path"].strip()
                # Remove '' introduced by terminal due to spaces
                if local_doc_path.startswith("'"):
                    local_doc_path = local_doc_path[1:]
                if local_doc_path.endswith("'"):
                    local_doc_path = local_doc_path[:-1]

                path_to_original = local_doc_path
                note.add_attachment(local_doc_path)

        metadata = {
            answers["document_name"]: {
                "document_name": answers["document_name"],
                "is_create_archive": answers["is_create_archive"],
                "document_location": answers["document_location"],
                "path_to_original": path_to_original,
            }
        }

        note.add_note_title_choice("Document", answers["document_name"])
        note.add_metadata("Document", metadata=metadata)

        # Check if user wants to add more
        questions = [
            {
                "type": "confirm",
                "name": "another_doc",
                "message": "Would you like to attach another document?",
            }
        ]
        is_another_doc = prompt(questions)["another_doc"]
        if not is_another_doc:
            break

    note.add_tags(["Document"])
