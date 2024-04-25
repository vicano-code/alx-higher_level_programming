#!/bin/bash
# sends a DELETE request to the URL passed as the first argument
# and displays the body of the response
# Usage: ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""

curl -sX DELETE "$1"
