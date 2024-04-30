#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
Usage: ./3-error_code.py http://0.0.0.0:5000/status_401
"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
