from neon_goby.clean import clean
from neon_goby.split import split

class NeonGoby(object):
  @staticmethod
  def parse(text):
    return split(clean(text))

  @staticmethod
  def clean(text):
    return clean(text)

  @staticmethod
  def split(text):
    return split(text)
