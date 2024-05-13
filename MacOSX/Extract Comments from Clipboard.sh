#!/bin/bash

# Navigate to the parent directory and then to the src directory to run the Python script
"${0%/*}/../python38/python" "${0%/*}/../src/ScrapeTikTokComments.py"

# Print a message in green color and reset the color
echo -e "\033[32m[*]\033[0m Press any key to close."

# Wait for user input to close
read -n 1 -s -r -p ""
