import holidays
from .mx_datetime import DateTime

__all__ = [
    'EasterSunday', 'CarnivalMonday', 'MardiGras', 'AshWednesday',
    'PalmSunday', 'EasterFriday', 'EasterMonday', 'Ascension', 'Pentecost',
    'WhitMonday', 'TrinitySunday', 'CorpusChristi', 'Ostersonntag',
    'DimanchePaques', 'Rosenmontag', 'Aschermittwoch', 'MercrediCendres',
    'Palmsonntag', 'DimancheRameaux', 'GoodFriday', 'Karfreitag',
    'VendrediSaint', 'Ostermontag', 'LundiPaques', 'Himmelfahrt',
    'WhitSunday', 'Pfingstsonntag', 'DimanchePentecote', 'Pfingstmontag',
    'LundiPentecote', 'Fronleichnam', 'FeteDieu'
]

_eastereggs = {}


def EasterSunday(year, country='iceland'):
    if year in _eastereggs:
        return _eastereggs[year]
    local_holidays = getattr(holidays, country, None)
    if local_holidays is None:
        raise ValueError('Holidays not available for {}.'.format(country))
    easter_dt = local_holidays.easter(year)

    _eastereggs[year] = d = DateTime(
        easter_dt.year, easter_dt.month, easter_dt.day)
    return d


# Some common feasts derived from Easter Sunday


def CarnivalMonday(year):
    return EasterSunday(year) - 48


def MardiGras(year):
    return EasterSunday(year) - 47


def AshWednesday(year):
    return EasterSunday(year) - 46


def PalmSunday(year):
    return EasterSunday(year) - 7


def EasterFriday(year):
    return EasterSunday(year) - 2


def EasterMonday(year):
    return EasterSunday(year) + 1


def Ascension(year):
    return EasterSunday(year) + 39


def Pentecost(year):
    return EasterSunday(year) + 49


def WhitMonday(year):
    return EasterSunday(year) + 50


def TrinitySunday(year):
    return EasterSunday(year) + 56


def CorpusChristi(year):
    return EasterSunday(year) + 60


Ostersonntag = EasterSunday
DimanchePaques = EasterSunday
Rosenmontag = CarnivalMonday
Aschermittwoch = AshWednesday
MercrediCendres = AshWednesday
Palmsonntag = PalmSunday
DimancheRameaux = PalmSunday
GoodFriday = EasterFriday
Karfreitag = EasterFriday
VendrediSaint = EasterFriday
Ostermontag = EasterMonday
LundiPaques = EasterMonday
Himmelfahrt = Ascension
WhitSunday = Pentecost
Pfingstsonntag = WhitSunday
DimanchePentecote = WhitSunday
Pfingstmontag = WhitMonday
LundiPentecote = WhitMonday
Fronleichnam = CorpusChristi
FeteDieu = CorpusChristi
