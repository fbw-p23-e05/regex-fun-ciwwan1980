# 7. Write a Python program to find sequences of lowercase letters joined by an underscore.
import re


input_string =   "Hello_world"

pattern = "[a-z]+_[a-z]+"

match = re.search(pattern, input_string)

if match:
    print("Match found:", match)
else:
    print("No match found.")