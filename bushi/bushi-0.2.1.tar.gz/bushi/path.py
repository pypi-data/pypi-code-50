import os

class path:

  @staticmethod
  def join(*args):
    return os.path.join(*args)

  @staticmethod
  def getdir():
    return os.getcwd()

  @staticmethod
  def changedir(*args):
    os.chdir(path.join(*args))

  @staticmethod
  def makedir(*args):
    os.makedirs(path.join(*args))

  @staticmethod
  def isdir(*args):
    return os.path.isdir(path.join(*args))

  @staticmethod
  def isfile(*args):
    return os.path.isfile(path.join(*args))

  @staticmethod
  def dirname(*args):
    return os.path.dirname(path.join(*args))