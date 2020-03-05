import calendar
import logging
import datetime
from icalendar import Calendar, Event, Alarm


class CurriculumParser:
    TIME_TABLE = {
        "1": datetime.timedelta(hours=8, minutes=15),
        "2": datetime.timedelta(hours=9, minutes=10),
        "3": datetime.timedelta(hours=10, minutes=15),
        "4": datetime.timedelta(hours=11, minutes=10),
        "5": datetime.timedelta(hours=13, minutes=50),
        "6": datetime.timedelta(hours=14, minutes=45),
        "7": datetime.timedelta(hours=15, minutes=40),
        "8": datetime.timedelta(hours=16, minutes=45),
        "9": datetime.timedelta(hours=17, minutes=40),
        "10": datetime.timedelta(hours=19, minutes=20),
        "11": datetime.timedelta(hours=20, minutes=15),
        "12": datetime.timedelta(hours=21, minutes=10)
    }

    def __init__(self, provider, first_day):
        self.provider = provider
        self.stDate = self.setStDate(first_day)

    def setStDate(self, first_day):
        stDate = first_day
        stWeekday = calendar.weekday(stDate.year, stDate.month, stDate.day)
        if stWeekday != 0:
            stDate += datetime.timedelta(6-stWeekday)
        return stDate

    def getClassList(self):
        logging.info('正在获取课程清单...')
        r = self.session.get(self.CLASS_SCHEDULE_URL)
        return r.json()

    def getClassInterval(self, str):
        str = str.strip("0")
        zero_count = str.count("0")
        one_count = str.count("1")
        return 1 if one_count == 1 else 1+zero_count//(one_count-1)

    def getClassTime(self, classmark):
        return self.TIME_TABLE.get(classmark)

    def getEndWeek(self, str):
        return str.rfind("1")+1

    def getStartWeek(self, str):
        return str.find("1")+1

    def getClassCount(self, str):
        return str.count("1")

    def dict2Event(self, item):
        event = Event()

        event.add('summary', item['coureName'])
        event.add('location', item['campusName'] +
                  item['teachingBuildingName']+item['classroomName'])
        event.add('dtstart', self.stDate + datetime.timedelta((self.getStartWeek(
            item['classWeek'])-1)*7 + int(item['classDay'])) + self.getClassTime(str(item['classSessions'])))
        event.add('dtend', self.stDate + datetime.timedelta((self.getStartWeek(item['classWeek'])-1)*7 + int(
            item['classDay'])) + self.getClassTime(
                str(int(item['classSessions'])+int(item['continuingSession'])-1))+datetime.timedelta(minutes=45))
        interval = self.getClassInterval(item['classWeek'])
        event.add('description', '课程号: ' +
                  item['coureNumber']+'\n课序号: '+item['coureSequenceNumber'])
        alarm = Alarm()
        alarm.add('action', 'DISPLAY')
        alarm.add('TRIGGER', datetime.timedelta(minutes=-15))
        event.add_component(alarm)
        if interval >= 0:
            event.add('rrule', {
                'freq': 'weekly', 'interval': interval,
                'count': self.getClassCount(item['classWeek'])
            })
        return event

    def phase(self):
        logging.info('正在创建日历...')
        classList = self.provider.getClassList()
        cal = Calendar()
        cal['version'] = '2.0'
        if self.stDate.month >= 7:
            cal['X-WR-CALNAME'] = str(self.stDate.year)+'年秋季课表'
        else:
            cal['X-WR-CALNAME'] = str(self.stDate.year)+'年春季课表'
        for course in classList['dateList'][0]['selectCourseList']:
            if(course['timeAndPlaceList'] is None):
                continue
            for item in course['timeAndPlaceList']:
                tempEvent = self.dict2Event(item)
                tempEvent['description'] += '\n教师: ' + \
                    course['attendClassTeacher']
                cal.add_component(tempEvent)
        logging.info('日历创建已完成...')
        return cal
