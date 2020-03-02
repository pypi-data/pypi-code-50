from PyInquirer import prompt
import email
import os
import re
import logging
import quopri
import pendulum


def clean_email_body(email_body: str) -> str:
    # Handles strings like '=20'
    decoded_email_body = quopri.decodestring(email_body).decode("utf-8")

    cleaned_email_body = ""

    for line in decoded_email_body.split("\n"):
        assert (
            "=20" not in line
        ), f"Found an unremoved whitespace indicator in line {line}"
        assert not line.endswith(
            "="
        ), f"Found an unremoved whitespace indicator in line {line}"
        if line.startswith(">"):
            cleaned_email_body += ">" + line + "\n"
        else:
            cleaned_email_body += "> " + line + "\n"

    logging.debug(f"Email body cleaned as: {cleaned_email_body}")
    return cleaned_email_body


def parse_email_file(email_path: str) -> dict:
    email_str = ""
    with open(email_path, "r") as fh:
        email_str = fh.read()

    msg = email.message_from_string(email_str)

    cc = str(msg["Cc"])
    cc = cc.replace("\n", " ")
    cc = cc.replace("\r", " ")

    email_date = pendulum.from_format(msg["Date"], "ddd, DD MMM YYYY HH:mm:ss ZZ")

    email_dict = {
        "To": msg["To"],
        "From": msg["From"],
        "CC": cc,
        "Subject": msg["Subject"],
        "Date": email_date,
    }

    if msg.is_multipart():
        # Only get the most recent email
        email_dict["Body"] = msg.get_payload()[0].as_string()
    else:
        email_dict["Body"] = msg.get_payload().as_string()

    logging.debug(f"Email body parsed as: {email_dict['Body']}")

    email_dict["Body"] = clean_email_body(email_dict["Body"])

    return email_dict


def generate_email(note):
    while True:

        questions = [
            {
                "type": "input",
                "name": "email_path",
                "message": "Path to the .eml file:",
            }
        ]

        answers = prompt(questions)

        email_path = answers[
            "email_path"
        ].strip()  # Strip due to whitespace introduced by terminal

        # Remove '' introduced by terminal due to spaces
        if email_path.startswith("'"):
            email_path = email_path[1:]
        if email_path.endswith("'"):
            email_path = email_path[:-1]

        assert os.path.exists(email_path), f"Could not find file: {email_path}"
        note.add_attachment(email_path)

        email_dict = parse_email_file(email_path)

        email_string = f"""
### {email_dict['Subject']}
{email_dict['Body']}
"""

        metadata = {
            email_dict["Subject"]: {
                "To": email_dict["To"],
                "From": email_dict["From"],
                "CC": email_dict["CC"],
                "Subject": email_dict["Subject"],
                "Date": email_dict["Date"],
                "Parsed From": email_path,
            }
        }
        note.add_note_title_choice("Email", email_dict["Subject"], email_dict["Date"])

        note.add_section("Email", email_string, tags=["Email"], metadata=metadata)

        # Check if user wants to add more
        questions = [
            {
                "type": "confirm",
                "name": "another_email",
                "message": "Would you like to add another_email?",
            }
        ]
        is_another_email = prompt(questions)["another_email"]
        if not is_another_email:
            break
