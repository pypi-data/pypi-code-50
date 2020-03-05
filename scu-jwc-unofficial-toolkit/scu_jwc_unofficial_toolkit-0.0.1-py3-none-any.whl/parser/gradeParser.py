from abc import abstractmethod
from typing import Iterable
from ..entity.gradeRecord import GradeRecord, CourseType
from ..entity.exam import ExamType


class GradeParser:

    @abstractmethod
    def parse(self, grade_info) -> Iterable[GradeRecord]:
        """将记录解析成成绩记录对象的迭代器
        """


class DefaultGradeParser(GradeParser):
    def parse(self, grade_info):
        for grade in grade_info["list"]["records"]:
            yield GradeRecord(
                term=grade[0],
                course_num=grade[1],
                course_index=grade[2],
                name=grade[11],
                en_name=grade[12],
                credit=grade[13],
                hour_num=grade[14],
                score_num=grade[8],
                score_level=grade[17],
                course_type=CourseType(grade[15]),
                exam_type=ExamType(grade[16])
            )
