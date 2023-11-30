#!/bin/bash
# takes in a URL, sends a POST request, and displays the response
curl -s -X POST -d "email=test@gmail&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
