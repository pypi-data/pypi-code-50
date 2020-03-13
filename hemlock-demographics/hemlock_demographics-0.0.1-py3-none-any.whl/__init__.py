"""Demographics

Adds demographics items to a page. Items are callables which take a page and 
add a demographics question.
"""

from hemlock import *

def demographics(page, *items, require=False):
    demographics_qs = [item(page) for item in items]
    if require:
        [Validate.require(q) for q in demographics_qs]