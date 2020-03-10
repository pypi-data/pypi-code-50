import logging
class LogException:
   def log_and_raise_exception(self,err_msg):
   
      '''
      Logs the error message and raises an exception
      :param err_msg
      '''
      logging.error(err_msg)
      raise Exception(err_msg)
      
      
      
