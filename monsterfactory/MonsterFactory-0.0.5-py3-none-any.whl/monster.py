import itertools
from math import ceil
from MonsterFactory.monster_lib import *


class Monster:

    def __init__(self, cr=None, m_rank=None):
        self.cr = CR(cr) if cr else CR(front_linear(28) + plus_or_minus_gauss(3))
        self.tier = self.cr.tier
        self.rank = m_rank or rank_by_tier(str(self.tier))
        self.name = random_monster(self.rank)
        variance = plus_or_minus_gauss(self.tier)
        self.ac = monster_stats["AC"][self.cr.key] + variance
        self.att = monster_stats["ATT"][self.cr.key] - variance
        self.hp_range = monster_stats["HP Range"][self.cr.key]
        lo, hi = self.hp_range
        self.hp = distribution_range(middle_linear, lo, hi) - (variance * self.tier)
        self.hp = ceil(self.hp * type_modifier(self.rank))
        self.dc = monster_stats["DC"][self.cr.key] + variance
        self.damage_range = monster_stats["Damage Range"][self.cr.key]
        lo, hi = self.damage_range
        self.dam = distribution_range(middle_linear, lo, hi) + (variance * self.tier)
        self.xp = ceil(monster_stats["XP"][self.cr.key] * type_modifier(self.rank))

    def get_data(self):
        return {
            "Name": self.name,
            "Tier": self.tier,
            "CR": self.cr.string,
            "Rank": self.rank,
            "Health": self.hp,
            "Armor Class": self.ac,
            "Attack Bonus": self.att,
            "Save DC": self.dc,
            "Typical Damage": self.dam,
            "XP Value": self.xp,
        }

    def __str__(self):
        output = (f"{k}: {v}" for k, v in self.get_data().items())
        return '\n'.join(itertools.chain(output, ("",)))


if __name__ == '__main__':
    for _ in range(3):
        m = Monster(3, m_rank="Minion")
        print(m)
