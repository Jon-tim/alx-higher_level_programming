#!/bin/bash
# takes in a URL as an argument, sends a GET request and displays response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
