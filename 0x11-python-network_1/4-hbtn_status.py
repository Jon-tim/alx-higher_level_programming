#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    res = req.text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- contenti: {res}")
