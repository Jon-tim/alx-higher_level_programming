#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL;
displays the value of the X-Request-Id variable found in the header
"""
import sys
import urllib.request

if __name__ == "__main__":
    arg = sys.argv[1]
    req = urllib.request.Request(arg)
    with urllib.request.urlopen(req) as response:
        result = response.getheader('X-Request-Id')
        print(result)
