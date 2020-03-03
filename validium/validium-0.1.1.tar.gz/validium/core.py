class Validator:

  def __init__(self, predicate, msg=None):

    assert callable(predicate), "the argument 'predicate' must be callable"
    assert msg is None or isinstance(msg, str), "the argument 'msg' must be None or an instance of str"

    self.__dict__ = dict(
      predicate=predicate,
      msg=msg,
    )

  def validate(self, target):
    assert self.predicate(target), self.msg