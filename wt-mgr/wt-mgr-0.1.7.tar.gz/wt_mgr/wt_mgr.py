import logging
import argparse
import pandas as pd
import numpy as np
import re
import os
import asyncio
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.exceptions import ApiError, AccessTokenError
from distutils.util import strtobool
from tabulate import tabulate
try:
    import constants
except ImportError:
    from wt_mgr import constants

# init logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logging.basicConfig()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# set console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)


try:
    # init WT API connection
    logger.info(f"Initializing WT API")
    api = WebexTeamsAPI()
    # pull all known teams and rooms
    all_teams = [ team for team in api.teams.list()]
    teams_by_id = { team.id: team.name for team in all_teams }
    teams_by_name = { team.name: team for team in all_teams }
    all_rooms = [ room for room in api.rooms.list() ]
except (AccessTokenError, ApiError) as e:
    logger.error(f"Failed to init WT API: {e}")
    exit(1)


def filter_df(df, options):
    if options.only_inactive:
        df = df[df.is_active == False]
        what = "only inactive"
    elif not options.include_inactive:
        df = df[df.is_active == True]
        what = "only active"
    else:
        what = "all"

    logger.info(f"Processing {what} elements from config.")
    return df


def create_teams(teams_df):
    """
    Process the teams DF and create Teams if not yet existing.
    """
    teams_set = teams_df.team_name.unique()

    for team_name in teams_set:
        logger.info(f"Creating team '{team_name}'")
        create_team(team_name)

    return

      
def create_team(team_name):
    team = teams_by_name.get(team_name)
    if not team:
        try:
            api.teams.create(team_name)
        except ApiError as e:
            logger.error(f"Error deleting team {team_name}: {e}")
    else:
        logger.warning(f"Team '{team_name}' already exists.")
    return


def delete_teams(teams_df):
    """
    Read the input DF file and delete Teams.
    """    
    teams_set = teams_df.team_name.unique()

    for team_name in teams_set:
        logger.info(f"Deleting team '{team_name}'")
        delete_team(team_name)
    return


def delete_team(team_name):
    team = teams_by_name.get(team_name)
    if team:
        try:
            api.teams.delete(team.id)
        except ApiError as e:
            logger.error(f"Error deleting team {team_name}: {e}")
    else:
        logger.warning(f"Team {team_name} not found.")


def create_rooms(rooms_df):
    """
    Process the rooms DF and create Rooms if not yet existing.
    """
    for _, room in rooms_df.iterrows():
        room_name = room.room_name
        team_name = room.team_name
        logger.info(f"Creating room '{room_name}' in '{team_name}'")
        create_room(room_name, team_name)
    return

      
def create_room(room_name, team_name):
    team = teams_by_name.get(team_name)
    if team:
        try:
            api.rooms.create(room_name, team.id)
        except ApiError as e:
            logger.error(f"Error creating room {room_name}: {e}")
        else:
            logger.warning(f"Room '{room_name}' already exists.")


def map_users_to_teams(teams_users_df):
    """
    Map users to teams
    """
    for _, account in teams_users_df.iterrows():
        team = teams_by_name.get(account.team_name)
        if team:
            add_mail_to_team(account.member_mail, team, account.is_moderator)
    return


def add_mail_to_team(mail, team, is_moderator=False):
    team_name = team.name
    logger.info(f"Adding {mail} to team: {team_name}{' as moderator' if is_moderator else ''}")
    try:
        api.team_memberships.create(team.id, personEmail=mail, isModerator=is_moderator)
    except ApiError as e:
        logger.error(f"Error: {e}")
    return


def get_teams_membership(teams_df):
    memberships = []
    teams_set = teams_df.team_name.unique()
    for team_name in teams_set:
        team = teams_by_name.get(team_name)
        if team:
            try:
                members = api.team_memberships.list(teamId=team.id)
                for member in members:
                    entry = {
                        "team_name": team.name,
                        "member_mail": member.personEmail,
                        "member_name": member.personDisplayName,
                        "is_active": True,
                        "is_moderator": member.isModerator
                    }
                    memberships.append(entry)
            except ApiError as e:
                pass

    memberships_df = pd.DataFrame(memberships)

    return memberships_df


def dump_teams_membership(df, out_path, backup=True):
    if not df.empty:
        if backup and os.path.isfile(out_path):
            backup_path = f"{out_path}.bak"
            os.rename(out_path, backup_path)
        df.to_csv(out_path, index=False)
    return


def add_eurl_to_rooms(rooms_df, default_room_only=True, config_room=True):
    # Keep only "General" room (room name == team name)
    if default_room_only:
        rooms_df = rooms_df[rooms_df.room_name == rooms_df.team_name]

    for _, room in rooms_df.iterrows():
        logger.info(f"Adding {constants.EURL_BOT_MAIL} to room {room.room_name} in team {room.team_name}")
        try:
            api.memberships.create(room.room_id, personEmail=constants.EURL_BOT_MAIL, isModerator=True)
        except ApiError as e:
            logger.error(f"Error: {e}")

        if config_room:
            config_room_eurl(room)
    return


def config_room_eurl(room, cmds=["list off", "internal off", "url"]):
        for cmd in cmds:
            logger.info(f"Sending '{cmd}' to room: {room.room_name} in {room.team_name}")
            try:
                api.messages.create(room.room_id, markdown=f"<@personId:{constants.EURL_BOT_ID}|EURL> {cmd}")
            except ApiError as e:
                logger.error(f"Error: {e}")
        return


async def clean_msgs_room(room, msg):
    logger.info(f"Deleting '{msg.id}' from room: {room.title}")
    try:
        api.messages.delete(msg.id)
    except ApiError as e:
        logger.error(f"Error: {e}")
    return


async def clean_msgs_rooms(rooms_list):
    for room in rooms_list:
        messages = api.messages.list(room.id)
        for msg in messages:
            await clean_msgs_room(room.id, msg)
    return


async def send_msg(room_id, msg):
    try:
        api.messages.create(room_id, markdown=msg)
    except ApiError as e:
        logger.error(f"Error: {e}")
    return


async def get_last_eurl_msg(room_id, wait=2):
    try:
        msgs = None
        while not msgs:
            msgs = [ m for m in api.messages.list(room_id) if m.personId == constants.EURL_BOT_ID ]
            if not msgs:
                await asyncio.sleep(wait)
        return msgs[0].text
    
    except ApiError as e:
        logger.error(f"Error: {e}")
    return


async def get_room_to_url_map(rooms_df):
    url_maps = []
    for _, room in rooms_df.iterrows():
        msg = f"<@personId:{constants.EURL_BOT_ID}|EURL> url"
        await send_msg(room.room_id, msg)
        last_response = await get_last_eurl_msg(room.room_id)
        url = last_response[last_response.find("https"):]
        url_maps.append({"room_name": room.room_name, "room_url": url})

    url_maps_df = pd.DataFrame(url_maps)

    return url_maps_df


def print_df(df):
    print(tabulate(df, headers="keys", showindex=False))
    return


async def wt_mgr():
    parser = argparse.ArgumentParser()
    # paths and input files
    parser.add_argument("-wd", "--work-dir", required=True, help="Set work directory")
    parser.add_argument("--init", action="store_true", help="Initialize work directory with CSV templates")
    parser.add_argument("-tf", "--teams-file", help="Override the path or name of the Teams definition CSV file")
    parser.add_argument("-rf", "--rooms-file", help="Override the path or name of the Rooms definition CSV file")
    parser.add_argument("-tu", "--teams-users-file", help="Override the path or name of the Teams Users definition CSV file")

    # actions
    parser.add_argument("-tc", "--create-teams", action="store_true", help="Create Teams as defined on CSV file")
    parser.add_argument("-td", "--delete-teams", action="store_true", help="Delete Teams as defined on CSV file")
    parser.add_argument("-rc", "--create-rooms", action="store_true", help="Create Rooms as defined on CSV file")
    parser.add_argument("-rd", "--delete-rooms", action="store_true", help="Delete Rooms as defined on CSV file")
    parser.add_argument("-ua", "--assign-users", action="store_true", help="Assign users to teams as defined on CSV file")
    parser.add_argument("-ur", "--remove-users", action="store_true", help="Remove users from teams as defined on CSV file")
    parser.add_argument("-ea", "--add-eurl", action="store_true", help="Add the EURL bot to the Teams rooms")
    parser.add_argument("-er", "--remove-eurl", action="store_true", help="Add the EURL bot to the Teams rooms")

    # show actions
    parser.add_argument("-ts", "--show-teams", action="store_true", help="Show Teams")
    parser.add_argument("-rs", "--show-rooms", action="store_true", help="Show Rooms")
    parser.add_argument("-us", "--show-users", action="store_true", help="Show Users")
    parser.add_argument("-gm", "--get-members", action="store_true", help="")
    parser.add_argument("-dm", "--dump-members", action="store_true", help="")
    parser.add_argument("-du", "--dump-urls", action="store_true")
    parser.add_argument("-sa", "--show-all", action="store_true")

    # options
    parser.add_argument("-ia", "--include-active", action="store_true")
    parser.add_argument("-ii", "--include-inactive", action="store_true")
    parser.add_argument("-oi", "--only-inactive", action="store_true")
    parser.add_argument("-sd", "--skip-dump", action="store_true", help="If selected, CSV files are NOT updated with live data.")
    parser.add_argument("-ic", "--import-current", action="store_true", help="Import existing teams/spaces/users from the WT account in use.")
    parser.add_argument("-fa", "--force-active", action="store_true", help="Used to mark existing teams/spaces to be imported in active state.")

    # filters
    parser.add_argument("--team-filter")
    parser.add_argument("--room-filter")
    parser.add_argument("--mail-filter")
    options = parser.parse_args()

    # process the data dir and input config files
    work_dir_override = os.path.isdir(options.work_dir) or options.init

    if not work_dir_override and not options.init:
        logger.error(f"Work directory {options.work_dir} doesn't exist: use --init to create and initialize the work directory.")
        exit(1)

    # teams
    teams_dir, teams_file = os.path.split(options.teams_file or constants.FNAME_TEAMS)
    teams_file_path = os.path.join(options.work_dir if work_dir_override else teams_dir, teams_file)
    # rooms
    rooms_dir, rooms_file = os.path.split(options.rooms_file or constants.FNAME_ROOMS)
    rooms_file_path = os.path.join(options.work_dir if work_dir_override else teams_dir, rooms_file)
    # teams_users
    teams_users_dir, teams_users_file = os.path.split(options.teams_users_file or constants.FNAME_TEAMS_USERS)
    teams_users_file_path = os.path.join(options.work_dir if work_dir_override else teams_dir, teams_users_file)

    # Initialize work dir
    if options.init:
        logger.info(f"Initializing work dir: {options.work_dir}")
        if not os.path.isdir(options.work_dir):
            os.mkdir(options.work_dir)
        for config_file, data in constants.DATA_SCHEMA.items():
            config_file_path = os.path.join(options.work_dir, data.get("filename"))
            config_file_schema = data.get("schema")
            if not os.path.isfile(config_file_path):
                logger.info(f"Creating file: {config_file_path}")
                with open(config_file_path, "w") as cfile:
                    csv_header = ",".join(list(config_file_schema.keys()))
                    cfile.write(f"{csv_header}\n")
        exit()

    # generate DFs out of lists and dicts
    all_teams_df = pd.DataFrame(
        [
            {
            "team_name": team.name,
            "team_id": team.id
            }
            for team in all_teams
        ]
    )

    all_rooms_df = pd.DataFrame(
        [
            {
                "room_name": room.title,
                "room_id": room.id,
                "team_id": room.teamId
            }
            for room in all_rooms
        ]
    )

    if options.show_all:
        logger.info(f"Showing current teams")
        print_df(all_teams_df)
        logger.info(f"Showing current rooms")
        print_df(all_rooms_df)

    # Teams
    if teams_file_path:
        logger.info(f"Importing teams config from: {teams_file_path}")
        teams_df = pd.read_csv(teams_file_path)
        teams_schema = constants.DATA_SCHEMA.get("teams").get("schema")
        logger.debug(f"schema: {teams_schema}")
        teams_df.astype(teams_schema)

        if not all_teams_df.empty:
            teams_df = pd.merge(
                teams_df, all_teams_df, 
                on="team_name",
                how="left",
                suffixes=("_old", "")
                )
            try:
                teams_df = teams_df.drop("team_id_old", axis=1)
            except KeyError:
                pass

        if options.import_current:
            logger.info("Importing current teams")
            if options.force_active:
                all_teams_df["is_active"] = True
            teams_df = teams_df.append(all_teams_df)

        teams_df.is_active.fillna(value=False, inplace=True)
        # teams_df.team_id.fillna(value="", inplace=True)
        # teams_df.team_description.fillna(value="", inplace=True)

        teams_df = filter_df(teams_df, options)

        if options.team_filter:
            t_filter = "|".join(options.team_filter.split(","))
            teams_df = teams_df[teams_df.team_name.str.contains(t_filter)]
        
        teams_df.drop_duplicates(inplace=True)

        teams_set = pd.Series(teams_df.team_name.unique()).to_list()
        teams_set_str = ",".join(teams_set)

        if options.show_all or options.show_teams:
            print_df(teams_df)
    
        if options.create_teams:
            logger.info("Creating Teams")
            create_teams(teams_df)

        if options.delete_teams:
            # to-do: verify this
            delete_teams(teams_df)

        if not options.skip_dump and not teams_df.empty:
            logger.info("Dumping teams DF to CSV")
            os.rename(teams_file_path, f"{teams_file_path}.bak")
            teams_df.to_csv(teams_file_path, index=False)
    
    # Rooms
    if rooms_file_path:
        logger.info(f"Importing rooms config from: {rooms_file_path}")
        rooms_df = pd.read_csv(rooms_file_path)
        rooms_df.team_name.fillna(value=teams_set_str, inplace=True)
        # rooms_df.is_active.fillna(value=False, inplace=True)
        # rooms_df.room_id.fillna(value="", inplace=True)
        # rooms_df.team_id.fillna(value="", inplace=True)
    
        # the "team_name" can be a list of team names
        rooms_df.team_name = rooms_df.team_name.str.split(",")
        rooms_df = rooms_df.explode("team_name")

        # fill the "General" room name from team (CSV has a line with empty team and room names)
        rooms_df.room_name.fillna(rooms_df.team_name, inplace=True)

        # join with `teams_df` to populate `team_id`
        if not teams_df.empty:
            rooms_df = pd.merge(
                rooms_df, teams_df[["team_name", "team_id"]], 
                on="team_name",
                how="left",
                suffixes=("_old", "")
                )
            rooms_df = rooms_df.drop("team_id_old", axis=1)

        # join with `all_rooms_df` to populate `room_id`
        if not all_rooms_df.empty:
            rooms_df = pd.merge(
                rooms_df, all_rooms_df[["room_name", "room_id", "team_id"]], 
                on=["room_name", "team_id"],
                how="left",
                suffixes=("_old", "")
                )
            rooms_df = rooms_df.drop("room_id_old", axis=1)

        if options.import_current:
            logger.info("Importing current rooms")
            all_rooms_df = pd.merge(
                all_rooms_df, teams_df[["team_name", "team_id"]], 
                on="team_id",
                how="left",
                suffixes=("_old", "")
            )
            if options.force_active:
                all_rooms_df["is_active"] = True

            rooms_df = rooms_df.append(all_rooms_df)

        rooms_df.is_active.fillna(value=False, inplace=True)
        rooms_df.room_id.fillna(value="", inplace=True)
        rooms_df.team_id.fillna(value="", inplace=True)

        rooms_df = filter_df(rooms_df, options)
        rooms_df.drop_duplicates(inplace=True)

        if options.team_filter:
            t_filter = "|".join(options.team_filter.split(","))
            rooms_df = rooms_df[rooms_df.team_name.str.contains(t_filter)]
        
        if options.room_filter:
            r_filter = "|".join(options.room_filter.split(","))
            rooms_df = rooms_df[rooms_df.room_name.str.contains(m_filter)]

        if options.show_all or options.show_rooms:
            print_df(rooms_df)
    
        if options.create_rooms:
            logging.info("Creating Rooms")
            create_rooms(rooms_df)
        
        if not options.skip_dump and not rooms_df.empty:
            logger.info("Dumping rooms DF to CSV")
            os.rename(rooms_file_path, f"{rooms_file_path}.bak")
            rooms_df.to_csv(rooms_file_path, index=False)

    # Teams users
    if teams_users_file_path:
        logger.info(f"Importing teams users config from: {teams_users_file_path}")
        teams_users_df = pd.read_csv(teams_users_file_path)

        if options.import_current:
            teams_users_df = teams_users_df.append(
                get_teams_membership(teams_df)
            )

        teams_users_df.team_name.fillna(value="", inplace=True)
        teams_users_df.member_mail.fillna(value="", inplace=True)
        teams_users_df.member_name.fillna(value="", inplace=True)
        teams_users_df.is_active.fillna(value=False, inplace=True)
        teams_users_df.is_moderator.fillna(value=False, inplace=True)

        teams_users_df = filter_df(teams_users_df, options)
        teams_users_df.drop_duplicates(inplace=True)

        if options.show_all or options.show_users:
            print_df(teams_users_df)

        if options.assign_users:
            map_users_to_teams(teams_users_df)

        if not options.skip_dump and not teams_users_df.empty:
            logger.info("Dumping teams users DF to CSV")
            os.rename(teams_users_file_path, f"{teams_users_file_path}.bak")
            teams_users_df.to_csv(teams_users_file_path, index=False)

    # Memberships
    if options.get_members or options.dump_members:
        members_df = get_teams_membership(teams_df)

        print_df(members_df)

        if options.dump_members:
            dump_teams_membership(members_df, teams_users_file_path)

    # Eurl
    if options.add_eurl:
        add_eurl_to_rooms(rooms_df)

    if options.dump_urls:
        url_map_df = await get_room_to_url_map(rooms_df)
        print_df(url_map_df)

    #await clean_msgs_rooms(rooms)
    
    return


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wt_mgr())


if __name__ == "__main__":
    main()
    