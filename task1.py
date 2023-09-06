

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).


import re


input_string = "Hello123Whatever6565665"

pattern = "^[a-zA-Z0-9]+$"


print(re.search(input_string,pattern))# this is wrong way, i shall use pattern in fits place
print(re.search(pattern, input_string))