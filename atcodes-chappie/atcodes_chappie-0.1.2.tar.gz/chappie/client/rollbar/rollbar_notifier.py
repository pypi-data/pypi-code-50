""" Rollbar Notifier """
import sys
import os


import rollbar


class RollbarNotifier():
    """
        from chappie.utils import RollbarNotifier
    """

    def publish_exception(cls, exception_info, e, level='info', extra_data={}):    # pragma: no cover
        """ Publish exception details to rollbar """
        (exc_type, exc_obj, exc_tb) = exception_info

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        message = {
            'Error': str(exc_type),
            'Source File': str(fname),
            'Line Number': str(exc_tb.tb_lineno),
            'Details': str(e)
        }

        for index, value in extra_data.items():
            message[index] = str(value)

        if os.environ.get('ENV') != 'local':
            rollbar.report_exc_info(extra_data=extra_data)
        else:
            print(message)

        return True


    def publish_message(cls, message, level='info', extra_data={}):
        """ Send a simple message to rollbar """
        message = {
            'message': message
        }
        message.update(extra_data)
        if os.environ.get('ENV') != 'local':
            rollbar.report_message('Got an IOError in the main loop', 'warning')
        else:
            print(message)

        return True
