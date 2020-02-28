"""Utilities used by minipam"""
import ipaddress
import string


def isip(ipstring):
    """Quick and dirty IPv4 validator"""
    if not isinstance(ipstring, str):
        raise TypeError('ipstring must be a string')
    try:
        ipaddress.ip_address(ipstring)
        return True
    except ValueError:
        return False


def ismac(macstring):
    """Quick and dirty MAC validator"""
    if not isinstance(macstring, str):
        raise TypeError('macstring must be a string')
    stripchar = [' ', ':', '-', '.', '0x']
    for char in stripchar:
        macstring = macstring.replace(char, '')
    hexcheck = [char in string.hexdigits for char in macstring]
    if (False not in hexcheck) and \
            ((len(hexcheck) == 12) or (len(hexcheck) == 16)):
        return True
    return False


def format_mac(macstring, delimiter=':', upper=False):
    """Format MAC address with the delimiter"""
    if not isinstance(macstring, str):
        raise TypeError('macstring must be a string')
    if not ismac(macstring):
        raise ValueError(macstring + ' is not a MAC address')
    stripchar = [' ', ':', '-', '.', '0x']
    for char in stripchar:
        macstring = macstring.replace(char, '')
    if delimiter not in stripchar[:-1]:
        raise ValueError('delimiter must be one of ' + str(stripchar[:-1]))
    octets = [a+b for a, b in zip(macstring[::2], macstring[1::2])]
    formatted_macstring = delimiter.join(octets)
    if upper:
        return formatted_macstring.upper()
    return formatted_macstring.lower()
