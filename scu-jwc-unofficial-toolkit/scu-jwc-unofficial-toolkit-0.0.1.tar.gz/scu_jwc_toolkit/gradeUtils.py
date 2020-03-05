import logging


class GradeUtil:
    def __init__(self, provider):
        self.provider = provider

    def weighted_avg(self):
        """加权平均分
        """

        logging.debug("total score={}".format(
            sum(map(lambda x: x.credit*x.score.to_num(), self.provider.get_grade()))))
        return sum(map(lambda x: x.credit*x.score.to_num(), self.provider.get_grade()))/self.total_credits()

    def total_credits(self):
        """总学分
        """
        i_grades = self.provider.get_grade()
        return sum(map(lambda x: x.credit, i_grades))
