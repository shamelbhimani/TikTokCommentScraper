#!/bin/bash

# Navigate to the parent directory and then to the src directory to run the Python script
# Since the script is in the 'MacOSX' subfolder under 'TikTokCommentScraper'
"${0%/*}/../python38/python" "${0%/*}/../src/CopyJavascript.py"

# Print a message in green color and reset the color
echo -e "\033[32m[*]\033[0m Press any key to close."

# Pause for 2 seconds (similar to double timeout in the batch script)
sleep 2
