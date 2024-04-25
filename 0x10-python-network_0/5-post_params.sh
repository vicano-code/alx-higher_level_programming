#!/bin/bash
# takes in a URL, sends a POST request with variable email&subject; Usage: ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
