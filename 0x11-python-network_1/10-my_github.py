#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""

from sys import argv
import requests


if __name__ == "__main__":
    username = argv[1]
    access_token = argv[2]
    headers = {
        "Authorization": f"token {access_token}"
    }
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:

