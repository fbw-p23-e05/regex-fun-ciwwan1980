# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
import re

input_string = "ab"

pattern = '^ab?$'

match = re.search(pattern, input_string)

if match:
    print("Match found:", match)
else:
    print("No match found.")