
# 2. Write a Python program that matches a string that has an a followed by zero or more b's.

import re

input_string = "abbbbb abb ab a"

pattern = 'ab*' # it matches a and zero or more b
pattern = 'ab+' # it matches a and at least one b
pattern = 'ab?' # it matches a and zero or only one b
match = re.findall(pattern, input_string)

if match:
    print("Match found:", match)
else:
    print("No match found.")
