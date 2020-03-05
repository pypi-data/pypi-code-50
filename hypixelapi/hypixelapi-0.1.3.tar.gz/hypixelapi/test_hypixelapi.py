import unittest
import requests
import argparse
import sys
from hypixelapi import HypixelAPI, PlayerNotFoundError, HypixelError

class TestHypixelAPI(unittest.TestCase):

    TOKEN = ""

    @classmethod
    def setUpClass(self):
        # INSERT YOUR OWN VALUES HERE
        self.api = HypixelAPI(self.TOKEN)
        self.player_uuid = "7b892af879f64e12a3ed6a895415212a"

    def test_get_player_json(self):
        malformed_uuid = "12345"
        invalid_player = "7b892af879f64e12a3ed6a895415212b"
        with self.assertRaises(HypixelError):
            self.api.get_player_json(malformed_uuid)
        with self.assertRaises(PlayerNotFoundError):
            self.api.get_player_json(invalid_player)
        resp = self.api.get_player_json(self.player_uuid)
        self.assertTrue(resp['player'] and resp['success'])

    def test_get_player_info(self):
        resp = self.api.get_player_json(self.player_uuid)
        self.assertTrue(resp)

    def get_all_skyblock_profiles(self):
        no_skyblock_stats = "63df014775a34346b38bfd0cf024b1ed"
        with self.assertRaises(HypixelError):
            self.api.get_all_skyblock_profiles(no_skyblock_stats)
        resp = self.api.get_all_skyblock_profiles(self.player_uuid)
        self.assertTrue(len(resp) == 2)

    def test_get_player_rank(self):
        admin = "f7c77d999f154a66a87dc4a51ef30d19"
        resp = self.api.get_player_rank(admin)
        self.assertTrue(resp['current_rank'] == "ADMIN")
        resp = self.api.get_player_rank(self.player_uuid)
        self.assertTrue(resp['current_rank'] == "MVP+")

    def test_get_boosters(self):
        resp = self.api.get_boosters()
        self.assertTrue(resp['success'] and resp['boosters'])

    def test_get_guild_by_name(self):
        resp = self.api.get_guild_by_name("Blue Crew")
        self.assertTrue(resp['success'] and resp['guild'] is not None)

    def test_get_guild_by_player(self):
        player_no_guild = "63df014775a34346b38bfd0cf024b1ed"
        resp = self.api.get_guild_by_player(self.player_uuid)
        self.assertTrue(resp['success'] and resp['guild'])
        resp = self.api.get_guild_by_player(self.player_uuid)
        self.assertTrue(resp['success'] and resp['guild'] is not None)

    def test_get_guild_by_guildid(self):
        guildid = "52e57a1c0cf2e250d1cd00f8"
        resp = self.api.get_guild_by_guildid(guildid)
        self.assertTrue(resp['success'] and resp['guild'] is not None)

    def test_get_friends(self):
        resp = self.api.get_friends(self.player_uuid)
        self.assertTrue(resp['success'] and resp['records'])

    def test_get_game_counts(self):
        resp = self.api.get_game_counts()
        self.assertTrue(resp['success'] and resp['games'])

    def test_get_leaderboards(self):
        resp = self.api.get_leaderboards()
        self.assertTrue(resp['success'] and resp['leaderboards'])

    def test_get_player_count(self):
        resp = self.api.get_game_counts()
        self.assertTrue(resp['success'] and resp['playerCount'] is not None)

    def test_get_resources(self):
        resource_list = ["achievements", "challenges",
            "quests", "guilds/achievements", "guilds/permissions",
            "skyblock/collections", "skyblock/skills"]
        for item in resource_list:
            resp = self.api.get_resources(item)
            self.assertTrue(resp['success'] and resp['lastUpdated'] is not None)

    def test_get_watchdog_stats(self):
        resp = self.api.get_watchdog_stats()
        self.assertTrue(resp['success'] and resp['watchdog_total'] is not None)

    def test_get_skyblock_auctions_by_player(self):
        resp = self.api.get_skyblock_auctions_by_player(self.player_uuid)
        self.assertTrue(resp['success'] and resp['auctions'] is not None)

    def test_get_skyblock_profile_by_profileid(self):
        profile = "16ffee3b157b427192e888f01fd128ce"
        resp = self.api.get_skyblock_profile_by_profileid(profile)
        self.assertTrue(resp['success'] and resp['auctions'] is not None)

    def test_get_skyblock_profile_by_profileid(self):
        profile = "16ffee3b157b427192e888f01fd128ce"
        resp = self.api.get_skyblock_auctions_by_profileid(profile)
        self.assertTrue(resp['success'] and resp['auctions'] is not None)

    def test_get_skyblock_profile_by_auctionid(self):
        auction_id = "886d01f4465b4efba180269cfffb07a7"
        resp = self.api.get_skyblock_auctions_by_auctionid(auction_id)
        self.assertTrue(resp['success'] and resp['auctions'] is not None)

    def test_get_current_skyblock_auctions(self):
        resp = self.api.get_current_skyblock_auctions(page=1)
        self.assertTrue(resp['success'] and resp['auctions'] is
            not None and resp['page'] == 1)

    def test_get_skyblock_news(self):
        resp = self.api.get_skyblock_news()
        self.assertTrue(resp['success'] and resp['items'] is not None)

    def get_skyblock_profile_by_profileid(self):
        profile = "16ffee3b157b427192e888f01fd128ce"
        resp = self.api.get_skyblock_profile_by_profileid(profile,
            self.player_uuid)
        self.assertTrue(resp['success'] and resp['profile'] is not None and "members" not in resp['profile'])
        resp = self.api.get_skyblock_profile_by_profileid(profile)
        self.assertTrue(resp['success'] and resp['profile'] is not None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    TestHypixelAPI.TOKEN = args.input
    sys.argv[1:] = args.unittest_args
    unittest.main()
