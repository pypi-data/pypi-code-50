from .core import FrameValidator

def empty():
  return FrameValidator(lambda df: df.size == 0, 'dataframe must be empty')

not_empty = lambda : FrameValidator(
  lambda df: df.size > 0, 
  'dataframe must not be empty'
)

cols = lambda n : FrameValidator(
  lambda df: df.shape[1] == n, 
  'dataframe must have {} cols'.format(n)
)

def rows(n):
  return FrameValidator(lambda df: df.shape[0] == n, 'dataframe must have {} rows'.format(n))
