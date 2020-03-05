import bisect
from abc import abstractmethod
from enum import Enum


class ScoreLevel(Enum):
    pass


class ZhScoreLevel(ScoreLevel):
    EXCELLENT = "优秀"
    GOOD = "良好"
    AVERAGE = "中等"
    QUALIFIED = "合格"
    PASS = QUALIFIED
    FAILED = "不合格"


class EnScoreLevel(ScoreLevel):
    A = "A"
    Aminus = "A-"
    Bplus = "B+"
    B = "B"
    Bminus = "B-"
    Cplus = "C+"
    C = "C"
    Cminus = "C-"
    Dplus = "D+"
    D = "D"
    F = "F"


class AbstractScore:
    """成绩抽象类
    """

    def __init__(self, score):
        self.score = score

    @abstractmethod
    def to_num(self) -> float:
        """返回百分制的成绩
        """

    def has_en_lavel(self):
        """该成绩记录是否应该有英语等级
        """

        return True

    @abstractmethod
    def to_en_level(self) ->EnScoreLevel:
        """返回英语等级制(A/A-/B/...)的成绩
        """

    @abstractmethod
    def to_zh_level(self) -> ZhScoreLevel:
        """返回中文等级制(优秀/良好/...)的成绩
        """

    @abstractmethod
    def to_point(self):
        """返回绩点制的成绩
        """

    def __float__(self):
        return self.to_num()

    def __str__(self):
        return self.to_zh_level()

    def __repr__(self):
        return f"<score {self.score.to_num()}>"


class NumericScore(AbstractScore):
    """数值型成绩

    转换算法参照《四川大学本科生等级成绩、百分制成绩、成绩绩点对照表》中，2017-2018秋季学期及以后部分之规定
    """

    BREAKPOINT = [60, 61, 63, 66, 70, 73, 76, 80, 85, 90]
    EN_WORDS = [EnScoreLevel.F, EnScoreLevel.D, EnScoreLevel.Dplus,
                EnScoreLevel.Cminus, EnScoreLevel.C, EnScoreLevel.Cplus,
                EnScoreLevel.Bminus, EnScoreLevel.B, EnScoreLevel.Bplus,
                EnScoreLevel.Aminus, EnScoreLevel.A]
    POINTS = [0, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4]
    ZH_BREAKPOINT = [60, 70, 76, 85]
    ZH_WORDS = [ZhScoreLevel.FAILED, ZhScoreLevel.PASS,
                ZhScoreLevel.AVERAGE, ZhScoreLevel.GOOD, ZhScoreLevel.EXCELLENT]

    def __init__(self, score: float):
        super().__init__(score)

    def to_num(self):
        return self.score

    def to_en_level(self):
        return self.EN_WORDS[bisect.bisect_right(self.BREAKPOINT, self.score)]

    def to_zh_level(self):
        return self.ZH_WORDS[bisect.bisect_right(self.ZH_BREAKPOINT, self.score)]

    def to_point(self):
        return self.POINTS[bisect.bisect_right(self.BREAKPOINT, self.score)]


class FormerNumericScore(NumericScore):
    """2017-2018秋季学期前的数值型成绩

    转换算法参照《四川大学本科生等级成绩、百分制成绩、成绩绩点对照表》中，2017-2018秋季学期以前部分之规定
    """

    BREAKPOINT = [60, 65, 70, 75, 80, 85, 90, 95]
    POINTS = [0, 1, 1.7, 2.2, 2.7, 3.2, 3.6, 3.8, 4]

    def has_en_lavel(self):
        """2017-2018秋季学期以前，根据教务处文件，没有提供英语形式的等级
        """
        return False


class LevelScore(AbstractScore):
    """等级型数据，兼容中英文

    转换算法参照《四川大学本科生等级成绩、百分制成绩、成绩绩点对照表》中，2017-2018秋季学期及以后部分之规定
    """

    LEVEL_TO_NUM = {
        EnScoreLevel.A: 95,
        EnScoreLevel.Aminus: 87,
        EnScoreLevel.Bplus: 82,
        EnScoreLevel.B: 77.5,
        EnScoreLevel.Bminus: 74,
        EnScoreLevel.Cplus: 71,
        EnScoreLevel.C: 67.5,
        EnScoreLevel.Cminus: 64,
        EnScoreLevel.Dplus: 61.5,
        EnScoreLevel.D: 60,
        EnScoreLevel.F: 0,
        ZhScoreLevel.EXCELLENT: 92.5,
        ZhScoreLevel.GOOD: 80,
        ZhScoreLevel.AVERAGE: 72.5,
        ZhScoreLevel.PASS: 64.5,
        ZhScoreLevel.FAILED: 0
    }

    def __init__(self, level: str or ScoreLevel):
        """可以传入等级枚举或者
        """

        if not isinstance(level, ScoreLevel):
            import re
            level = EnScoreLevel(level) if re.match(
                "[A-F][+-]?", level) else ZhScoreLevel(level)
        super().__init__(level)

    def to_num(self):
        return self.LEVEL_TO_NUM[self.score]

    def to_en_level(self):
        return NumericScore(self.LEVEL_TO_NUM[self.score]).to_en_level()

    def to_zh_level(self):
        return NumericScore(self.LEVEL_TO_NUM[self.score]).to_zh_level()

    def to_point(self):
        return NumericScore(self.LEVEL_TO_NUM[self.score]).to_point()


class FormerLevelScore(LevelScore):
    """2017-2018秋季学期以前的等级型成绩

    转换算法参照《四川大学本科生等级成绩、百分制成绩、成绩绩点对照表》中，2017-2018秋季学期以前部分之规定
    """
    LEVEL_TO_NUM = {
        ZhScoreLevel.EXCELLENT: 92.5,
        ZhScoreLevel.GOOD: 80,
        ZhScoreLevel.AVERAGE: 72.5,
        ZhScoreLevel.PASS: 64.5,
        ZhScoreLevel.FAILED: 0
    }
