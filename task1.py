

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


import re


input_string = "Hello123Whatever6565665"

pattern = "^[a-zA-Z0-9]+$"


if re.match(pattern, input_string):
    print("The string contains only allowed characters,capital and small letter-number 0-9 .")
else:
    print("The string contains other characters.")
