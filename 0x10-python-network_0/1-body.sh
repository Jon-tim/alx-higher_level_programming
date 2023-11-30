#!/bin/bash
# takes in a URL, sends a GET request, displays the body of the response
curl -sfL -X GET "$1"
