#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
use the GitHub API:
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos"
    req = requests.get(f"{url}/{owner}/{repo}/commits")
    res = req.json()
    for commit in range(1, 11):
        sha = res[commit].get('sha')
        author = res[commit].get('commit').get('author').get('name')
        print(f"{sha}: {author}")
