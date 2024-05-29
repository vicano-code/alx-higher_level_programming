#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    payload = {'q': q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        dict = r.json()
        if dict:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
