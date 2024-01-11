#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    basic = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user"
    req = requests.get(url, auth=basic)
    res = req.json()
    print(res.get('id'))
