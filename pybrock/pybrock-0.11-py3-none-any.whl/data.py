import pandas as pd
import numpy as np
import string
from brock import utils


# letters
def letters(upper=False, n=None):
  # the data
  if upper:
    l = list(string.ascii_uppercase)
  else:
    l = list(string.ascii_lowercase)
  # if n, how many to randomly sample
  if n > 0:
    l = np.random.choice(l, n)
  
  l = list(l)
  return( l )

  
# state_name
def state_name():
  # get the dict names from states in brock utils module
  s = utils.states()
  # return 
  return(s.keys())
    
  
# state_abbreviation
def state_abb():
  # get the dict names from states in brock utils module
  s = utils.states()
  # return 
  return(s.values())
