

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


import re


input_string = "Hello123Whatever6565665....."

pattern = "^[a-zA-Z0-9]+$"

match= re.search(pattern, input_string)
print(match)

for char in input_string:
    if not re.search(pattern, char):
        print(f"The character '{char}' does not match the pattern.")

