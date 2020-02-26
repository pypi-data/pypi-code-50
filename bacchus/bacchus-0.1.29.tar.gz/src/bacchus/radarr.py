import json
import sqlite3
import xml.etree.ElementTree as ET

from .base import HomeServerApp


class Radarr(HomeServerApp):
    @property
    def config_file(self):
        return self.path / 'config.xml'

    @property
    @lru_cache()
    def config(self):
        return ET.parse(str(self.config_file))

    def setup_nginx(self):
        self.config.find('UrlBase').text = '/movies/'
        self.config.write(str(self.config_file))

    def setup_indexers(self):
        api_key = json.loads((self.path / '..' / 'jackett' / 'Jackett' /
                              'ServerConfig.json').read_text())['APIKey']
        indexers = []
        for prov in (TEMPLATES / 'jackett' / 'Indexers').glob('*.json'):
            name = prov.stem.lower()
            indexers.append({
                'Name':
                name,
                'Implementation':
                'Torznab',
                'Settings':
                json.dumps({
                    "minimumSeeders":
                    1,
                    "requiredFlags": [],
                    "baseUrl":
                    f"https://private.{self.domain}/trackers/api/v2.0/indexers/{name}/results/torznab/",
                    "multiLanguages": [],
                    "apiKey":
                    apikey,
                    "categories": [
                        5010, 5030, 5040, 2000, 2010, 2020, 2030, 2035, 2040,
                        2045, 2050, 2060
                    ],
                    "animeCategories": [],
                    "removeYear":
                    False,
                    "searchByTitle":
                    False,
                }),
                'ConfigContract':
                'TorznabSettings',
                'EnableRss':
                1,
                'EnableSearch':
                1
            })

        conn = sqlite3.connect(str((self.path / 'nzbdrone.db').absolute()))
        cursor = conn.cursor()
        for indexer in indexers:
            cursor.execute('insert into Indexers values (?, ?, ?, ?, ?, ?)',
                           indexer.values())
        conn.commit()
        conn.close()

    def setup(self):
        self.setup_nginx()
        if self.container:
            self.container.stop()
        self.setup_indexers()
        self.compose.start()
