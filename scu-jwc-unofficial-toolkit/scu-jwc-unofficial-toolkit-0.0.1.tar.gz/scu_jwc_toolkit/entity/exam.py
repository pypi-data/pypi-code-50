import enum


class ExamType(enum.Enum):
    """考试类型
    """
    TEST = "考试"  # 考试
    INSPECT = "考查"  # 考察
    NONE = None  # 空白
