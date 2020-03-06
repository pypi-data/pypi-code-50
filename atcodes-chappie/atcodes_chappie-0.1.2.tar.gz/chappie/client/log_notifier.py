import os


from chappie.client.rollbar import RollbarNotifier


class LogNotifier():
    def __init__(self, *args, **kwargs):
        super(LogNotifier, self).__init__(*args, **kwargs)

        self.notifier_service = os.environ.get('CHAPPIE_NOTIFIER_SERVICE', 'rollbar')    

        if self.notifier_service  == "rollbar":
            self.client = RollbarNotifier()
        else:
            self.client = None
            raise ValueError("Notifier Service (%s) is not supported" % (self.notifier_service))

    def publish_exception(self, exception_info, e, level='info', extra_data={}):
        """  call method from the selected client """
        self.client.publish_exception(exception_info, e, level='info', extra_data={})
        return True

    def publish_message(self, message, level='info', extra_data={}):
        """  call method from the selected client """
        self.client.publish_message(message, level='info', extra_data={})
        return True
