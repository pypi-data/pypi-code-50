import logging
from typing import Iterable
from abc import abstractmethod
from functools import lru_cache
from ...entity.gradeRecord import GradeRecord, CourseType
from ...parser.gradeParser import DefaultGradeParser


class GradeFilter:
    """成绩过滤器类

    通过继承本类并定义validate方法，来定义过滤器的行为。
    clear方法为为过滤器提供了恢复初始状态的能力。
    过滤器支持&,|,~三种运算任意组合。
    """

    @abstractmethod
    def validate(self, grade_record: GradeRecord)->bool:
        """判断该成绩是否应该被视为有效的记录

        True表示应该被列为记录
        """

    def clear(self) -> None:
        pass

    def __and__(self, other):
        return AndFilter(self, other)

    def __or__(self, other):
        return OrFilter(self, other)

    def __invert__(self):
        return NotFilter(self)


class DefaultFilter(GradeFilter):
    def validate(self, grade_record):
        return True


class AndFilter(GradeFilter):
    """组合过滤器，用于支持两个过滤器的与运算
    """

    def __init__(self, A, B):
        super().__init__()
        self.A = A
        self.B = B

    def validate(self, grade_record):
        return self.A.validate(grade_record) and self.B.validate(grade_record)

    def clear(self):
        self.A.clear()
        self.B.clear()


class OrFilter(AndFilter):
    """组合过滤器，用于支持两个过滤器的或运算
    """

    def validate(self, grade_record):
        return self.A.validate(grade_record) or self.B.validate(grade_record)


class NotFilter(GradeFilter):
    """组合过滤器，用于支持两个过滤器的非运算
    """

    def __init__(self, A):
        self.A = A

    def clear(self):
        self.A.clear()

    def validate(self, grade_record):
        return not self.A.validate()


class FirstFilter(GradeFilter):
    """该过滤器在初始化后，仅允许第一次出现的课程号的成绩

    建议仅在带有排序能力的provider下使用。否则，第一次出现这个概念毫无意义。
    """

    def __init__(self):
        super().__init__()
        self.s = set()

    def validate(self, grade_record):
        if grade_record.course_num not in self.s:
            logging.debug(f"{grade_record.course_num} is not in set{self.s}")
            self.s.add(grade_record.course_num)
            return True
        logging.debug(f"{grade_record.course_num} is already in set{self.s}")
        return False

    def clear(self):
        self.s.clear()


class RequiredOnlyFilter(GradeFilter):
    """仅筛选出必修课的过滤器
    """

    def validate(self, grade_record):
        if grade_record.course_type == CourseType.REQUIRED:
            logging.debug(f"{grade_record} 是必修课!")
            return True
        else:
            logging.debug(f"{grade_record} 不是必修课!")
            return False


class AllGradeProvider:
    '''提供全部的成绩数据，包括多次选修
    '''
    ALL_SCORES_DATA = "http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/allTermScores/data"

    def __init__(self, auth_provider):
        self.session = auth_provider.login()
        self.parser = DefaultGradeParser()

    def get_grade(self)->Iterable:
        grade_info = self._get_grade_json()
        logging.debug(grade_info)
        return self.parser.parse(grade_info)

    @lru_cache()
    def _get_grade_json(self):
        logging.info("正在获取全部成绩信息...")
        r = self.session.post(self.ALL_SCORES_DATA, data={
            "pageNum": 1,
            "pageSize": 999
        })
        return r.json()


class GradeProvider(AllGradeProvider):
    def __init__(self, auth_provider, filter=DefaultFilter(), *args, **kwargs):
        super().__init__(auth_provider, *args, **kwargs)
        self.filter = filter

    def get_grade(self):
        all_grades = super().get_grade()
        self.filter.clear()
        for grade in all_grades:
            if self.filter.validate(grade):
                yield grade


class OrderedGradeProvider(GradeProvider):
    '''有序的成绩清单。默认为按照学期排序
    '''

    def __init__(self, auth_provider,  key=lambda x: x.term, *args, **kwargs):
        super().__init__(auth_provider,  *args, **kwargs)
        self.key = key

    def get_grade(self) -> Iterable:
        all_grades = sorted(super().get_grade(), key=self.key)
        return iter(all_grades)


class FirstGradeProvider(OrderedGradeProvider):
    '''按照教务处核算均分时的标准，所有成绩以第一次修读为准，同一课程号只能出现一次

    本质上和OrderedGradeProvider类没有任何区别，仅仅更换了过滤器。
    因此本类等价于OrderedGradeProvider(filter=FirstFilter())
    '''

    def __init__(self, auth_provider, filter=FirstFilter(), * args, **kwargs):
        super().__init__(auth_provider, filter=filter, *args, **kwargs)
