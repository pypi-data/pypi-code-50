class Validator:

  def __init__(self, predicate, fail_msg=None):

    assert callable(predicate), "the argument 'predicate' must be callable"
    assert fail_msg is None or isinstance(fail_msg, str), "the argument 'fail_msg' must be None or an instance of str"

    self.__dict__ = dict(
      predicate=predicate,
      fail_msg=fail_msg,
    )

  def validate(self, target):
    assert self.predicate(target), self.fail_msg