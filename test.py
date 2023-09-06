# import re


# pattern = 'end$'

# # List of example strings
# example_strings = ["The end", "The weekend", "Ending", "End of the line"]

# for string in example_strings:
#     match = re.search(pattern, string)
#     if match:
#         print(f"Match found: {string} - {match}")
#     else:
#         print(f"No match found: {string}")

import re

pattern = "[^abc]"

# Input strings
input_string1 = "apple"
input_string2 = "banana"
input_string3 = "cherry"
input_string4 = "bca"

# Check if the pattern matches any character that is not 'a', 'b', or 'c'
match1 = re.search(pattern, input_string1)
match2 = re.search(pattern, input_string2)
match3 = re.search(pattern, input_string3)
match4 = re.search(pattern, input_string4)

if match1:
    print(f"Match 1 found: '{match1.group()}'")
else:
    print("Match 1 not found.")

if match2:
    print(f"Match 2 found: '{match2.group()}'")
else:
    print("Match 2 not found.")

if match3:
    print(f"Match 3 found: '{match3.group()}'")
else:
    print("Match 3 not found.")

if match4:
    print(f"Match 4 found: '{match4.group()}'")
else:
    print("Match 4 not found.")
