#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    res = req.text
    print(
        f"Body response:\n"
        f"\t- type:{type(res)}\n"
        f"\t- content: {res}\n"
    )
