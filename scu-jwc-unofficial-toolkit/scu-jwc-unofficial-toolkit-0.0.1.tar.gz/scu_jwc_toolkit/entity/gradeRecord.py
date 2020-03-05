from typing import Optional
import enum
from .score import NumericScore, LevelScore, FormerLevelScore, FormerNumericScore


class GradeRecord:
    """学生成绩类
    term: 学期号
    course_num: 课程号
    course_index: 课序号
    name: 课程名
    en_name: 课程英文名
    credit: 学分
    hour_num: 学时
    score: 成绩
    course_type: 课程类型
    exam_type: 考试类型
    """

    def __init__(
        self,
        term: str,
        course_num: str,
        course_index: str,
        name: str,
        en_name: str,
        credit: int,
        hour_num: int,
        score_num: float,
        score_level: str,
        course_type: Optional,
        exam_type: Optional
    ):
        self.term = term
        self.course_num = course_num
        self.course_index = course_index
        self.name = name
        self.en_name = en_name
        self.credit = credit
        self.hour_num = hour_num
        self.course_type = course_type
        self.exam_type = exam_type
        score = None
        # 如果学期早于2017-2018年秋季学期
        if tuple(map(int, term.split("-"))) < (2017, 2018, 1, 1):
            score = FormerNumericScore(
                score_num) if score_num else FormerLevelScore(score_level)
        else:
            score = NumericScore(
                score_num) if score_num else LevelScore(score_level)
        self.score = score

    def __repr__(self):
        return f"<GradeRecore {self.term} | {self.name} | {self.credit} | {self.score.to_num()}>\n"


class CourseType(enum.Enum):
    """课程类型
    """
    REQUIRED = "必修"  # 必修课
    OPTIONAL = "选修"  # 选修课
    INTEREST = "任选"  # 任选课
