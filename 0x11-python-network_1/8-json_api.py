#!/usr/bin/python3
"""
A Python script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    req = requests.post(url, data={'q': q})
    try:
        res = req.json()
        if res and 'id' in res and 'name' in res:
            print(f"[{res.get('id')}] {res.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
