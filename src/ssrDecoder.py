# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:07:35 2018

@author: kmykoh97
"""




import base64
import sys


def to_bytes(s):
    if bytes != str:
        if type(s) == str:
            return s.encode('utf-8')
        
    return s



def to_str(s):
    if bytes != str:
        if type(s) == bytes:
            return s.decode('utf-8')
        
    return s



def ssrIsValid(link):
    return link[:6] == 'ssr://'



def base64_decode(string):
    def adjust_padding(string):
        """Adjust to base64 format, i.e. len(string) % 4 == 0."""
        missing_padding = len(string) % 4
        if missing_padding:
            string += '=' * (4 - missing_padding)
        return string

    string = adjust_padding(string.strip())
    
    return to_str(base64.urlsafe_b64decode(to_bytes(string)))



def decoder(link):
    if not ssrIsValid(link):
        raise Exception(link + 'is not a valid ssr link')
    
    # link[6:] to strip the first 6 characters, i.e. 'ssr://'
    config_str = base64_decode(link[6:]).split('/?')

    required_config = config_str[0].split(':')
    optional_config = config_str[1]

    config = {}
    config['server'] = required_config[0]
    config['server_port'] = required_config[1]
    config['protocol'] = required_config[2]
    config['method'] = required_config[3]
    config['obfs'] = required_config[4]
    config['password'] = base64_decode(required_config[5])
    for param in optional_config.split('&'):
        if param:  # remove empty param
            k, v = param.split('=')
            try:
                config[k] = base64_decode(v)
            except Exception:  # in case that this is not a base64encoded string, use the original string instead.
                config[k] = v

    return config