import json

from achievements import Achievements


class Exporter:
    async def generate_achievement_export(self, achievement_class: Achievements = Achievements()):
        achievements = await achievement_class.get_for_user('saitho#2703')

        json_data = {
            "release_per_platform_id": "battlenet_5272175",
            "achievements": []
        }
        for achievement in achievements:
            json_data['achievements'].append({
                "name": achievement['name'],
                "description": achievement['description'],
                "api_key": achievement['api_key'],
                "image_url_unlocked": achievement['image_url'],
                "image_url_locked": None
            })

        with open('exports/gog-overwatch-achievements_all.json', 'w') as outfile:
            json.dump(json_data, outfile)