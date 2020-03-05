import requests
import json
from urllib.parse import quote

class HypixelAPI():
    """The HypixelAPI class used for calling all functions related to the API."""

    def __init__(self, key):
        """Initalises the HypixelAPI class with the desired arguments.

        :param key: Your Hypixel API access token (retrieve one by using /api on
            the Hypixel server).
        """
        self.token = key
        self.url = "https://api.hypixel.net/"

    def get_player_json(self, uuid):
        """Gets the full JSON of a player by their UUID.

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: Player's full JSON
        """
        r = requests.get(self.url + "player?uuid=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_player_info(self, uuid):
        """Gets some basic information about a player.

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: Player's displayname, uuid, rank and possibly social media
            and karma.
        """
        resp = self.get_player_json(uuid)
        player_dict = {}
        player = resp['player']
        player_dict['uuid'] = strip_uuid(uuid)
        player_dict['displayname'] = player['displayname']
        player_dict['rank'] = self.__retrieve_rank(resp)
        try:
            player_dict['socialMedia'] = player['socialMedia']['links']
        except KeyError:
            pass
        try:
            player_dict['karma'] = player['karma']
        except KeyError:
            pass
        return player_dict

    def get_all_skyblock_profiles(self, uuid):
        """Retrieves all Skyblock profiles for a single player.

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: A dictionary of all the user's Skyblock profiles
        """
        resp = self.get_player_json(uuid)
        profiles = {}
        player = resp['player']
        if "stats" in player:
            if "SkyBlock" in player['stats']:
                if "profiles" in player['stats']['SkyBlock']:
                    profiles = player['stats']['SkyBlock']['profiles']
        if not profiles:
            raise HypixelError('SkyBlock stats not found!')
        final_dict = {}
        for key, value in profiles.items():
            r = requests.get(self.url + "skyblock/profile?profile=" + key + "&key=" + self.token)
            resp = json.loads(r.text)
            final_dict[key] = resp['profile']['members'][strip_uuid(uuid)]
        return final_dict

    def get_player_rank(self, uuid):
        """Gets rank information about a player.

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: Player's rank information (including current_rank and
            underlying_rank) as a dictionary
        """
        resp = self.get_player_json(uuid)
        return self.__retrieve_rank(resp)

    def get_boosters(self):
        """Gets full JSON data about boosters

        :returns: All current booster information as a dictionary
        """
        r = requests.get(self.url + "boosters?key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_guild_by_name(self, name):
        """Finds guild information by name

        :param name: The name of a guild
        :returns: The guild information as a dictionary
        """
        r = requests.get(self.url + "guild?name=" + quote(name) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_guild_by_player(self, uuid):
        """Retrieves guild information by member UUID

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: The guild information as a dictionary
        """
        r = requests.get(self.url + "guild?player=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_guild_by_guildid(self, uuid):
        """Retrieves guild information by guild ID

        :param uuid: A guild UUID
        :returns: The guild information as a dictionary
        """
        r = requests.get(self.url + "guild?id=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    """
    def find_guild_by_uuid(self, uuid):
        r = requests.get(self.url + "findGuild?byUuid=" + uuid + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)
    """

    def get_friends(self, uuid):
        """Finds friends of a player.

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: A list of the player's friends as a dictionary
        """
        r = requests.get(self.url + "friends?uuid=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_game_counts(self):
        """Gets information about the number of players in each gamemode.

        :returns: Gamemode's player counts as a dictionary
        """
        r = requests.get(self.url + "gameCounts?key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_leaderboards(self):
        """Gets information about game's leaderboards.

        :returns: Gamemode's leaderboards as a dictionary
        """
        r = requests.get(self.url + "leaderboards?key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_player_count(self):
        """Returns the total number of players on the server

        :returns: Total number of players as a dictionary
        """
        r = requests.get(self.url + "playerCount?key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_resources(self, resource_type):
        """Gets information about static resources

        :returns: Resource data as a dictionary
        """
        r = requests.get(self.url + "resources/" + resource_type)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_session(self, uuid):
        """SOON TO BE REMOVED: Gets information about a player's session.

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: Player's session information as a dictionary
        """
        r = requests.get(self.url + "session?uuid=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_watchdog_stats(self):
        """Gets Watchdog statistics.

        :returns: Watchdog statistics as a dictionary
        """
        r = requests.get(self.url + "watchdogstats?key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)


    def get_skyblock_auctions_by_player(self, uuid):
        """Gets information about a player's auctions

        :param uuid: A player's UUID (either trimmed form or one with dashes)
        :returns: Player's auction data as a dictionary
        """
        r = requests.get(self.url + "skyblock/auction?player=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_skyblock_auctions_by_profileid(self, uuid):
        """Gets information about a Skyblock profile's auctions

        :param uuid: A Skyblock profile ID
        :returns: Profile's auction information as a dictionary
        """
        r = requests.get(self.url + "skyblock/auction?profile=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_skyblock_auctions_by_auctionid(self, uuid):
        """Gets information about a specific auction

        :param uuid: A Skyblock auction ID
        :returns: Auction information as a dictionary
        """
        r = requests.get(self.url + "skyblock/auction?uuid=" + strip_uuid(uuid) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)


    def get_current_skyblock_auctions(self, page=0):
        """Gets information about Skyblock's current auctions

        :param page: The page to retrieve (starting from 0,
            1000 results on each page)
        :returns: Current auction information as a dictionary
        """
        r = requests.get(self.url + "skyblock/auctions?page=" + str(page) + "&key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_skyblock_news(self):
        """Gets Skyblock news

        :returns: Skyblock news as a dictionary
        """
        r = requests.get(self.url + "skyblock/news?key=" + self.token)
        resp = json.loads(r.text)
        return self.__check_response(resp)

    def get_skyblock_profile_by_profileid(self, uuid, player_uuid=None):
        """Retrieves a Skyblock profile

        :param uuid: A Skyblock profile UUID
        :param player_uuid: A player UUID: only used if a singular player's
            data is wanted rather than all the members of the profile.
        :type player_uuid: str, optional
        :returns: A dictionary of the requested Skyblock profile
        """
        r = requests.get(self.url + "skyblock/profile?profile=" + uuid + "&key=" + self.token)
        resp = json.loads(r.text)
        self.__check_response(resp)
        if player_uuid is None:
            return resp
        else:
            return resp['profile']['members'][strip_uuid(player_uuid)]

    def __check_response(self, resp):
        """Private function used for checking if the request was successful

        :returns: The response if valid
        """
        if not check_success(resp):
            raise HypixelError(resp['cause'])
        if "player" in resp:
            if resp['player'] == None:
                raise PlayerNotFoundError("Player with specified UUID not found!")
        return resp

    def __retrieve_rank(self, resp):
        """Private function used for determining the rank of a player

        :returns: Rank information as a dictionary
        """
        rank = {}
        player = resp['player']
        if 'monthlyPackageRank' in player:
            if player['monthlyPackageRank'] == "SUPERSTAR":
                rank['current_rank'] = "MVP++"
        if 'rank' in player:
            if player['rank'] != "NORMAL":
                rank['current_rank'] = player['rank']
        if 'newPackageRank' in player:
            if "current_rank" in rank:
                rank['underlying_rank'] = player['newPackageRank'].replace("_PLUS", "+")
            else:
                rank['current_rank'] = player['newPackageRank'].replace("_PLUS", "+")
        if rank == {}:
            rank['current_rank'] == "Default"
        return rank


class HypixelError(Exception):
    """General error when something has gone wrong.
    Can be caught with ``except hypixelapi.HypixelError``"""
    pass

class PlayerNotFoundError(Exception):
    """Exception that is thrown when a player isn't found.
        Can be caught with ``except hypixelapi.PlayerNotFoundError``"""
    pass

def strip_uuid(uuid):
    return uuid.replace("-", "")

def check_success(resp):
    if "success" in resp:
        return resp['success']
    return False
