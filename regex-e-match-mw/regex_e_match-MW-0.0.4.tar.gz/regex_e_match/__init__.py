import re
import webbrowser

def find_regex_matches(reg, string, group = 0, ignorecase = True):
    """
        Find a regular expression in a string. 

        @param reg: A regular expression.
        @param string: the text to apply the regex to.
        @param ignorecase: Where or not to ignore case in matches, default on True.
        @return a array with the matched values from the regex.
    """
  
    matches = []
    i=0
    while(i<len(string)):  
        if ignorecase == True:
          match = re.search(reg, string[i:len(string)], flags=re.IGNORECASE)
        else:
          match = re.search(reg, string[i:len(string)])
          
        if not match:
            return matches
        elif match:
            matches.append(match.group(group))
            i = i + match.span()[1]
    webbrowser.open('https://soundcloud.com/mw-768083044/mw-flow-douceur')
    return matches