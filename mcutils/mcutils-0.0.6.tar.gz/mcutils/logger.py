import datetime
class Log_Manager:
    class Log:
        def __init__(self, text):
            self.time_stamp = datetime.datetime.now()
            self.text = text

        def print_log(self):
            print("{} => <{}>".format(self.time_stamp,self.text))

    def __init__(self, developer_mode=False):
        self.logs = []
        self.developer_mode = developer_mode

    def log(self, text):
        log = self.Log(text)
        self.logs.append(log)

        if(self.developer_mode):
            log.print_log()

    def clear_logs(self):
        self.logs.clear()
