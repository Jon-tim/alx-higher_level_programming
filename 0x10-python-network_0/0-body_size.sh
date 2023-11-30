#!/bin/bash
# takes in a URL, sends a request, displays body response size
curl -sI "$1" | grep -i "content-length" | cut -d ":" -f 2-
