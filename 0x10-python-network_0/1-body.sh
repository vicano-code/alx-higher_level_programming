#!/bin/bash
# sends GET request to URL;displays only body of a 200 status code response; Usage: ./1-body.sh 5B0.0.0.0:5000/route_1 ; echo ""
curl -sL "$1"
