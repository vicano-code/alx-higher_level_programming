#!/bin/bash
# uses curl to sends a GET request to the URL, and 
# displays the body of the response
# Display only body of a 200 status code response
# Usage: ./1-body.sh 5B0.0.0.0:5000/route_1 ; echo ""

curl -sL "$1"
