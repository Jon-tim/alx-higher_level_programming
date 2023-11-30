#!/bin/bash
# takes in a URL, sends a request, displays body response size
curl -w "%{size_download}\n"  -s "$1" 
