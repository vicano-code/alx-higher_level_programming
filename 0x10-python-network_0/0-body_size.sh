#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the 
# size in bytes of the body of the response
# Usage: ./0-body_size.sh 0.0.0.0:5000

body_size=$(curl -sI "$1" | grep 'Content-Length:' | cut -f2)
echo $body_size
