import re


pattern = 'end$'

# List of example strings
example_strings = ["The end", "The weekend", "Ending", "End of the line"]

for string in example_strings:
    match = re.search(pattern, string)
    if match:
        print(f"Match found: {string} - {match}")
    else:
        print(f"No match found: {string}")
