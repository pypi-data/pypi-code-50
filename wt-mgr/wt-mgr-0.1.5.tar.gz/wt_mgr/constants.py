EURL_BOT_MAIL = "eurl@sparkbot.io"
EURL_BOT_ID = "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wZjcwMDc1NC1iZDAxLTRiZjMtODMwZC0wZTZmNGEwZGQ0ODY"

FNAME_TEAMS = "teams.csv"
FNAME_ROOMS = "rooms.csv"
FNAME_TEAMS_USERS = "teams_users.csv"

SCHEMA_TEAMS = ["team_name","team_description","is_active","team_id"]
SCHEMA_ROOMS = ["room_name","team_name","is_active","room_id","team_id"]
SCHEMA_TEAMS_USERS = ["team_name", "member_mail", "member_name", "is_active", "is_moderator"]

DATA_SCHEMA = {
    "teams": {
        "filename": "teams.csv",
        "schema": {
            "team_name": str,
            "team_description": str,
            "is_active": bool,
            "team_id": str,
        },
    },
    "rooms": {
        "filename": "rooms.csv",
        "schema": {
            "room_name": str,
            "team_name": str,
            "is_active": bool,
            "room_id": str,
            "team_id": str
            },
    },
    "teams_users": {
        "filename": "teams_users.csv",
        "schema" : {
            "team_name": str,
            "member_mail": str,
            "member_name": str, 
            "is_active": bool, 
            "is_moderator": bool,
            },
    }
}