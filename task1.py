

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


import re

input_string = "helloThere  there there what are u doing"
pattern = "[a-zA-Z0-9]+$"


# $: This symbol matches the end of the string, ensuring that the pattern applies until the end of the string.

# if i remove $ signs, then every word will be appeared at least one time, because there isa sign of +, mean once or more time
matches = re.findall(pattern, input_string)

if matches: 
    for match in matches:
        print(f"Match found: {match}")
else:
    print("No matches found in the input string.")


