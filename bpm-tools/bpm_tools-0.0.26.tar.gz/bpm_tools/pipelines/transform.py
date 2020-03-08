try:
    import unzip_requirements
except ImportError:
    pass

import re

#Library to parse the user agent string
from user_agents import parse

# ------------- get_articlekey_from_url ------------------
#
#    Function extracts article key from a url 
#    
#    Returns:
#           articleid
#           newspaper_site (host)
#           articlekey (articleid + newspaper_site)
#    
#    Otherwise returns None
# ---------------------------------------------------------

pat_domain = r'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)'
pat_articleid = "\D(\d+b?)(.ece|_1.ece|.html|_1.html|.snd|_1.snd)"


def get_articlekey_from_path(data, url):

    #Get the articlekey
    try:
        articleid = re.search(pat_articleid, url).group(1)
        newspaper_site = re.search(pat_domain, url).group(1)
        articlekey = articleid + newspaper_site
        
    except Exception as e:
        return

    else:
        data['articleid'] = articleid
        data['newspaper_site'] = newspaper_site
        data['articlekey'] = articlekey
        
    return


# ------------- parse_user_agent------------------
#
#    Function parses as user agent string and returns
#    
#    device_type:  Mobile, Tablet or Desktop
#    device:  ex. iPhone, etc.
#    browser 
#    
# ---------------------------------------------------------


def parse_user_agent(userAgent):
    
    try:
        user_agent = parse(userAgent)
        
        if user_agent.is_mobile:
            device_type = 'Mobile'
        elif user_agent.is_tablet:
            device_type = 'Tablet'
        elif user_agent.is_pc:
            device_type = 'Desktop'
        else:
            device_type = 'Other'
        device = user_agent.device.family
        browser = user_agent.browser.family
    
    except:
        device = 'Unknown'
        browser = 'Unknown'
        device_type = 'Unknown'
    
    return device_type, device, browser

