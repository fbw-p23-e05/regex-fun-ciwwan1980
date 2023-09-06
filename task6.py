# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
import re


input_string = "abbb"

pattern = "ab{2,3}"

match = re.search(pattern, input_string)

if match:
    print("Match found:", match)
else:
    print("No match found.")