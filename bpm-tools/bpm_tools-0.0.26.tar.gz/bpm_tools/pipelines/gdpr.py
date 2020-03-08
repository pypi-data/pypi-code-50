import ast
import re
from datetime import datetime
from dateutil import parser
from urllib.parse import unquote

import boto3

#Hashing and regex
from hashlib import md5
import dateutil.parser
from copy import deepcopy



'''
# ---------------------------------------------------------

    hash_and_anonymise
    
    This function hashes and optionally anonymises the following keys
    in a json object:
    
    All keys ending in the word email or phone (Hashed/anonymised)
    All keys ending in birthdate (anonymised)
    All keys containing address or customer_name (anonymised)
    
    NOTE: This is a recursive function which alters the passed json
    
    If anonymise = True - The above fields are anonymised
    If anonymise = False - only hashing occurs
    
    keys_to_anonymise:  This is a list of dictionary keys for which
                        the correponding data is to be anonymised 
# ---------------------------------------------------------

'''

def hash_and_anonymise(y, anonymise = True, parent = None, keys_to_anonymise = None):
    
    #SETUP the custom anonymisation regex based on the passed keys_to_anonymise list
    try:
        
        if keys_to_anonymise is not None:
            anonymise_regex = r'(.*?)' + '|'.join(map(str, keys_to_anonymise)) 
        else:
            anonymise_regex = None
    except:
        anonymise_regex = None

    
    for k, v in y.copy().items():
            
            
        # ------------------------------------------------------------
        #Numeric type values (e.g. strings that are numbers or numbers)
        # are converted to string keeping only significant decimal points
        # e.g. 37.0 will be converted to 37, while 2.78 will be 2.78
        # https://stackoverflow.com/questions/2440692/formatting-floats-in-python-without-trailing-zeros
        #NOTE: Fix for scientific notation as per link above
        # ------------------------------------------------------------

        
        try:
            #HANDLE numeric string
            v_new = ('%f' % float(v)).rstrip('0').rstrip('.')
            y[k] = v_new

        except Exception as e:
            #ALL other are strings (except lists and dictionaries)
            if type(v) is not dict and type(v) is not list:
                y[k] = str(v)
        
        
        
        
        #Lower userId (just in case we till get uppercase ids)
        if k == 'userId':
            try:
                y[k] = v.lower()
            except:
                pass

        #Lower newspaper_shortcode (just in case we till get uppercase)
        elif re.match(r'(.*?)(newspaper_shortcode$)', k):
            try:
                y[k] = v.lower()
            except:
                pass
        
        
        elif k == 'birthdate':
            try:
                y['birth_year'] = str(dateutil.parser.parse(y[k]).year)
            except:
                i = 1
                #y['birth_year'] = None
                
            y[k] = None

        #IP Address - anonymise
        elif k.lower() == 'ip':
            y[k] = None

        #Extract the postalcode and country(Assuming that address is an array of dictionaries)
        #NOTE these values are attached to the parent nested dictionary (e.g. the properties)
        elif k == 'postalCode':
            try:
                parent['postalcode'] = v
            except:
                pass
        elif k == 'country':
            try:
                parent['country'] = v
            except:
                pass

        #Email and Phone fields (Hash and anonymise)
        elif re.match(r'(.*?)(email$|phone$|phone_number$|phonenumber_called)', k):
            if v is not None and v != '':
                y[k] = md5(str(v).encode('utf-8')).hexdigest()
            else:
                y[k] = None  

        #Address, birthdate and customer name fields (if anonymise=True)
        elif anonymise and re.match(r'(.*?)(address|birthdate$|customer_name)', k) is not None:
            y[k] = None

        #USER INPUTTED: Anonymise the fields contained in 
        elif anonymise_regex is not None and re.match(anonymise_regex, k) is not None:
            y[k] = None
            


        if type(v) is dict:
            #print(k)
            hash_and_anonymise(v,anonymise, parent = y)
        
        #Only parse list items which are of type dict or list (not strings or numbers)
        elif type(v) is list:
            for item in v:
                if type(item) is dict or type(item) is list:
                    hash_and_anonymise(item,anonymise, parent = y)



    
                    