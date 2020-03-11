import itertools
import pandas as pd

# ?expand.grid in R -- lite version
def expand_grid2(x, y, colnames=None):
    """
    A relatively comparable function to expand.grid in R from two list inputs.
    
    Returns a dataframe
    """
    
    # checks
    assert isinstance(x, list), "x is not a list"
    assert isinstance(y, list), "y is not a list"
    if colnames is not None:
      assert isinstance(colnames, list), "colnames is not a list"
    
    
    # create the cartesian product
    xy = list(itertools.product(x,y))
    if colnames:
      combos = pd.DataFrame(xy, columns=colnames)
    else:
      combos = pd.DataFrame(xy)
    
    # return the dataframe
    return(combos)



def expand_grid(cols=None, *itrs):
  """
  Take an arbitrary number of list inputs and return a dataframe.
  
  Parameters:
      cols (list): a list of column names, must be of same len as *itrs
  
  Returns a dataframe
  """
  
  # colname validation and definition
  if cols:
    assert isinstance(cols, list), "cols must be a list"
    assert len(cols) == len(itrs), "The number of column names must match the length of *itrs"
    cnames = cols
  else:
    cnames = ["var{}".format(i+1) for i in range(len(itrs))]
  
  # modified from: https://stackoverflow.com/a/12131385/155406
  product = list(itertools.product(*itrs))
  
  # make the dataframe
  df = pd.DataFrame(product, columns=cnames)
  return(df)


# helper to return a dict of state data
def states():
  # from https://gist.github.com/rogerallen/1583593
  us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
  
  # return
  return(us_state_abbrev)



