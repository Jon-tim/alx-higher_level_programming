#!/usr/bin/python3
"""
A Python script that takes in a URL;
Sends a request to the URL; and
Displays the body of the response (decoded in utf-8).
"""
import urllib
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.Request(url) as req:
        try:
            response = urllib.request.urlopen(req)
            html = response.read()
            print(html.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
