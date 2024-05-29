#!/bin/bash
# sends a request to a URL argument; displays only the response status code; Usage:./100-status_code.sh 0.0.0.0:5000 ; echo ""
curl -o /dev/null -w '%{http_code}' -sLI "$1"
