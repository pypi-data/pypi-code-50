import pyowm

"""
  See: https://github.com/csparpa/pyowm
"""


class Weather(object):
    def __init__(self, settings):
        self._cfg = settings["weather"]
        self._owm = pyowm.OWM(self._cfg["API_key"])

    @property
    def owm(self):
        return self._owm

    @property
    def observation(self):
        return self.owm.weather_at_place("Bremen,DE")

    @property
    def weather(self):
        return self.observation.get_weather()
