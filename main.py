import re
from datetime import datetime

# Function to extract date from a given text line
def extract_date(line):
    date_pattern = r'\d{4}-\d{2}-\d{2}'  # Regular expression for YYYY-MM-DD format
    match = re.search(date_pattern, line)
    if match:
        return datetime.strptime(match.group(), '%Y-%m-%d')
    return None

# Function to sort lines in a file by date
def sort_lines_by_date(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Extract dates and sort lines based on those dates
    sorted_lines = sorted(lines, key=extract_date)
    
    return sorted_lines

# Usage
filename = '/Users/artur/Desktop/NORD/tip1.txt'  # Change this to the path of your file
sorted_lines = sort_lines_by_date(filename)

# Optionally, write sorted lines to a file or print them
for line in sorted_lines:
    print(line.strip())
