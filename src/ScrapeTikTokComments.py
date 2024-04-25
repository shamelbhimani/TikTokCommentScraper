#!/usr/bin/env python3

import sys
import os
from csv import reader
from datetime import datetime as d
from pyperclip import paste, PyperclipException
from openpyxl import Workbook

# Get the current directory of the script
cur_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))  # Get the parent directory

# Define the output folder path one level up from the current directory
output_dir = os.path.join(parent_dir, 'output')

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize the prompt to support ANSI escape sequences
os.system("")

# Attempt to get CSV content from clipboard
try:
    csv = paste()
except PyperclipException:
    print("\x1b[31m[*]\x1b[0m Could not find copy/paste mechanism on this system. Please paste the CSV below and end the input with an empty line:")
    csv = '\n'.join(iter(input, ''))

# Write the CSV content to a file
csv_path = os.path.join(output_dir, "temporary.csv")
try:
    print("\x1b[34m[*]\x1b[0m Writing CSV from clipboard to file, removing carriage return characters ('\\r').", end='', flush=True)
    with open(csv_path, "w", encoding="utf-8") as file:
        file.write(csv.replace("\r", "\n").replace("\n\n", "\n"))
    print("\r\x1b[32m[*]\x1b[0m Writing CSV from clipboard to file completed.")
except Exception as e:
    print("\n\x1b[31m[X]\x1b[0m Couldn't write to CSV file:", str(e))
    sys.exit(1)

# Create an Excel workbook and worksheet
wb = Workbook()
ws = wb.active

# Convert CSV to Excel
try:
    print("\x1b[34m[*]\x1b[0m Converting CSV file to Excel Workbook (XLSX).", end='', flush=True)
    line_count = 0
    with open(csv_path, 'r', encoding="utf-8") as f:
        for row in reader(f):
            ws.append(row)
            line_count += 1
    print(f"\r\x1b[32m[*]\x1b[0m Converted {line_count} lines to Excel Workbook.")
except Exception as e:
    print("\n\x1b[31m[X]\x1b[0m Failed to convert CSV to Excel:", str(e))
    sys.exit(1)

# Request input for filename after conversion
input_name = input("Enter a name for the file: ")
xlsx_path = os.path.join(output_dir, f"Scrape_{input_name}_{d.now().strftime('%Y%m%d%H%M%S')}.xlsx")

# Save the Excel workbook
try:
    wb.save(xlsx_path)
    print(f"\r\x1b[32m[*]\x1b[0m Excel file saved as {xlsx_path}.")
except Exception as e:
    print("\n\x1b[31m[X]\x1b[0m Failed to save Excel file:", str(e))
    sys.exit(1)

# Delete the CSV file
try:
    os.remove(csv_path)
    print("\x1b[32m[*]\x1b[0m CSV file deleted.")
except Exception as e:
    print("\r\x1b[31m[*]\x1b[0m Could not delete CSV file:", str(e))

print("\x1b[32m[*]\x1b[0m Done.")
