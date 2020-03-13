"""Demographics items

# https://macses.ucsf.edu/research/socialenviron/sociodemographic.php
# see also Rad et al. 2018
"""

from hemlock import *

from datetime import datetime

"""Date of birth"""

def date_of_birth(page):
    # VALIDATE DATE IS LESS THAN TODAY
    i = Input(
        page, 
        label='<p>Please enter your date of birth.</p>',
        var='DateOfBirth',
        input_type='date',
        all_rows=True
    )
    Submit(i, compute_age, args=[page])
    return i

def compute_age(input, page):
    data = (
        None if input.data is None 
        else (datetime.utcnow() - input.data).days / 365.25
    )
    Embedded(page, var='Age', data=data, all_rows=True)

"""Gender"""

def gender(page):
    c = Check(
        page,
        label='<p>Please select your gender.</p>',
        var='Gender',
        all_rows=True,
        choices=['Male','Female','Other']
    )
    Submit(c, compute_male, args=[page])
    return c

def compute_male(check, page):
    data = None if check.data is None else int(check.data == 'Male')
    Embedded(page, var='Male', data=data, all_rows=True)

"""Race"""

def race(page):
    c = Check(
        page,
        label='<p>Please select your race/ethnicity. (Select as many as apply).</p>',
        var='Race',
        all_rows=True,
        choices=[
            'White/Caucasian',
            'Black/African American',
            'Asian',
            'Native American/Alaskan Native',
            'Hispanic/Latino',
            'Pacific Islander',
            'Other'
        ],
        multiple=True
    )
    return c