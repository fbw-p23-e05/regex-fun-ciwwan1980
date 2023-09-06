# 3. Write a Python program that matches a string that has an a followed by one or more b's.

import re

input_string = "ab"

pattern = 'ab+'

match = re.search(pattern, input_string)

if match:
    print("Match found:", match)
else:
    print("No match found.")
