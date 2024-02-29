#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -i -s "$1" | head -n 5 | tail -1 | grep -o -E '[0-9]+'  
