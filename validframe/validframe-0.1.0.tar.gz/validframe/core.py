import validium as V

def slice(df, rows = None, cols = None):
  if rows is None and cols is None:
    sliced_df = df
  elif rows is None and cols is not None:
    sliced_df = df[cols]
  elif rows is not None and cols is None:
    sliced_df = df.loc[rows]
  else: # both rows and cols is not None
    sliced_df = df.loc[rows, cols]
  return sliced_df
  
def itercells(df):
  cols = df.columns
  for row_idx, row in df.iterrows(): 
    for col_name in cols:
      yield df.loc[row_idx, col_name]
        
class SliceValidator(V.Validator):
  def __init__(self, predicate, fail_msg=None, cols=None, rows=None):
    super().__init__(predicate, fail_msg)
    
    self.cols = cols
    self.rows = rows
  
class FrameValidator(SliceValidator):
  def validate(self, df):
    sliced_df = slice(df, self.rows, self.cols)
    super().validate(sliced_df)

class CellsValidator(SliceValidator):
  def validate(self, df):
    sliced_df = slice(df, self.rows, self.cols)
    cells = itercells(sliced_df)
    super().validate(cells)


class RowsValidator(SliceValidator):
  def validate(self, df):
    sliced_df = slice(df, self.rows, self.cols)
    rows = sliced_df.iterrows()
    super().validate(rows)
