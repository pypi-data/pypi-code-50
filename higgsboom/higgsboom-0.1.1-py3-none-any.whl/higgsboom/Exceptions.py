class ExceptionWithMsg(Exception):
	def __init__(self, errorMsg):
		super().__init__(self)
		self.errorMsg = errorMsg

	def __str__(self):
		return self.errorMsg

class NoDataError(ExceptionWithMsg):
	pass

class ProcessFailure(ExceptionWithMsg):
	pass


