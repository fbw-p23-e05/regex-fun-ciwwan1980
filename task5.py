# 5. Write a Python program that matches a string that has an a followed by three 'b'.

import re


input_string = "abb"

pattern = "ab{3}"

match = re.search(pattern, input_string)

if match:
    print("Match found:", match)
else:
    print("No match found.")
