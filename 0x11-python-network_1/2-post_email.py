#!/usr/bin/python3
"""
A Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter;
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {'email' : mail}
    url_values = urllib.parse.urlencode(data).encode('utf-8')
    # print(url_values)
    req = urllib.request.Request(url, url_values, method='POST')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        dec = html.decode('utf-8')
        print(f"Your email is: {dec}")
