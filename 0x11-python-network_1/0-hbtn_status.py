#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(
            f"Body response:\n"
            f"\t- type: {type(html)}\n"
            f"\t- content: {html}\n"
            f"\t- utf8 content: {html.decode('utf-8')}"
        )
