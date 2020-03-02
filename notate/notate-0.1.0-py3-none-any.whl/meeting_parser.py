from PyInquirer import prompt
import re
import pendulum
import os
import icalendar


def parse_ical_file() -> dict:
    parse_ical_questions = [
        {"type": "input", "name": "ical_path", "message": "iCal file path: "}
    ]
    answers = prompt(parse_ical_questions)

    ical_path = answers["ical_path"].strip()

    # Remove '' introduced by terminal due to spaces
    if ical_path.startswith("'"):
        ical_path = ical_path[1:]
    if ical_path.endswith("'"):
        ical_path = ical_path[:-1]

    assert os.path.exists(ical_path), f"Failed to find iCal path: {ical_path}"
    with open(ical_path, "r") as fh:
        gcal = icalendar.Calendar.from_ical(fh.read())
        for component in gcal.walk():
            if component.name == "VEVENT":
                meeting_dict = dict()

                meeting_dict["meeting_name"] = component.get("summary")

                attendees = component.get("attendee")
                attendees_str = ""
                if attendees:
                    for attendee in attendees:
                        attendees_str += attendee.params["cn"] + ", "

                if attendees_str:
                    # cut off last " ,"
                    attendees_str = attendees_str[:-2]

                meeting_dict["attendees"] = attendees_str

                meeting_dict["location"] = component.get("location")
                meeting_dict["meeting_time"] = pendulum.instance(
                    component.get("dtstart").dt, tz="America/Los_Angeles"
                )
                meeting_dict["end_time"] = pendulum.instance(
                    component.get("dtend").dt, tz="America/Los_Angeles"
                )
                meeting_dict["description"] = component.get("description")
                meeting_dict["ical_path"] = ical_path
                return meeting_dict


def parse_ical_string() -> dict:
    # Example 1:
    # --------------------------------------------------------
    # Sync Meeting
    # Scheduled: Feb 1, 2024 at 10:00 AM to 11:00 AM
    # Location: Conference Room A; WebEx B
    #
    # Invitees: The Pope, Carl Sagan, Obama
    # The description is written here.
    #
    # Could span multiple lines with whitespace.
    #
    # --------------------------------------------------------
    # Example 2:
    # --------------------------------------------------------
    # Cars and Coffee
    # Scheduled: Feb 25, 2020 at 10:00 AM to 10:30 AM
    # Location: Chromatic Coffee
    # Invitees: Jay Leno <leno@garage.com>, Christian Koneggsieg <christian@oneggsieg.com>
    # --------------------------------------------------------
    # Example 3:
    # --------------------------------------------------------
    # All Day Event
    # Scheduled: Feb 2, 2020

    parse_ical_questions = [{"type": "input", "name": "ical", "message": "iCal string"}]
    answers = prompt(parse_ical_questions)

    ical_string = answers["ical"].strip()

    meeting_dict = dict()

    # Get Meeting Name
    ical_split = ical_string.split("\n")
    meeting_dict["meeting_name"] = ical_split[
        0
    ]  # First non-whitespace line is meeting name

    # Get Time and Date
    match_obj = re.search(r"(\w+ \d+, \d+)(.*)", ical_string)
    assert match_obj, f"Could not find date in {ical_string}"

    if match_obj.group(2):
        match_obj = re.search(r"(\w+ \d+, \d+) at (\d+:\d+ [AP]M)", ical_string)
        print(match_obj.group(1))
        meeting_dict["meeting_time"] = pendulum.from_format(
            f"{match_obj.group(1)} {match_obj.group(2)}",
            "MMM D, YYYY h:mm A",
            tz="America/Los_Angeles",
        )
    else:
        print(match_obj.group(0))
        meeting_dict["meeting_time"] = pendulum.from_format(
            match_obj.group(0), "MMM D, YYYY", tz="America/Los_Angeles"
        )

    # Get Attendees
    match_obj = re.search(r"Invitees:(.*)", ical_string)
    if match_obj:
        meeting_dict["attendees"] = match_obj.group(1).strip()

    # Get Location
    match_obj = re.search(r"Location:(.*)", ical_string)
    if match_obj:
        meeting_dict["location"] = match_obj.group(1).strip()

    return meeting_dict


def parse_manual_fields() -> dict:
    manual_entry = [
        {"type": "input", "name": "meeting_name", "message": "Meeting name?"},
        {
            "type": "input",
            "name": "attendees",
            "message": "Who attended the meeting (comma separated)?",
        },
        {"type": "input", "name": "location", "message": "Where was this meeting?"},
        {
            "type": "input",
            "name": "date",
            "message": "What day was this meeting in ISO format (e.x. 2020-02-18)?",
        },
        {
            "type": "input",
            "name": "time",
            "message": "What time was this meeting (e.x. 10:00 AM)?",
        },
    ]
    answers = prompt(manual_entry)

    meeting_dict = {
        "meeting_name": answers["meeting_name"],
        "attendees": answers["attendees"],
        "location": answers["location"],
        "meeting_time": pendulum.from_format(
            answers["date"].strip() + " " + answers["time"].strip(),
            "YYYY-MM-DD h:m A",
            tz="America/Los_Angeles",
        ),
    }

    return meeting_dict


def generate_meeting(note):
    while True:

        how_to_parse_fields = [
            {
                "type": "list",
                "name": "parse_type",
                "message": "How to get information about the meeting?",
                "choices": ["iCal File", "iCal String", "manual"],
            }
        ]

        answers = prompt(how_to_parse_fields)

        if answers["parse_type"] == "iCal File":
            meeting_dict = parse_ical_file()
            meeting_dict["parse_type"] = "ical file"
            assert (
                "ical_path" in meeting_dict
            ), f"Failed to find the path of the .ical file."
            note.add_attachment(meeting_dict["ical_path"])
        if answers["parse_type"] == "iCal String":
            meeting_dict = parse_ical_string()
            meeting_dict["parse_type"] = "ical string"
        elif answers["parse_type"] == "manual":
            meeting_dict = parse_manual_fields()
            meeting_dict["parse_type"] = "manual"

        note.add_note_title_choice(
            "Meeting", meeting_dict["meeting_name"], meeting_dict["meeting_time"]
        )

        metadata = {meeting_dict["meeting_name"]: meeting_dict}
        note.add_metadata("Meeting", metadata)
        note.add_tags(["Meeting"])

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
