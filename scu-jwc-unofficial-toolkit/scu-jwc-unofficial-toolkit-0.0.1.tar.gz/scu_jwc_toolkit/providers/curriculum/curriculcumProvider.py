import logging


class CurriculcumProvider:
    CLASS_SCHEDULE_URL = 'http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback'

    def __init__(self, auth_provider):
        self.session = auth_provider.login()

    def getClassList(self):
        logging.info('正在获取课程清单...')
        r = self.session.get(self.CLASS_SCHEDULE_URL)
        return r.json()
