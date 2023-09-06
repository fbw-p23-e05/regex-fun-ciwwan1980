# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re


pattern = "[A-Z][a-z]"

# only when all are uppercase, it will not match 

input_string = "ALLUPPERcASe"
matches = re.search(pattern, input_string)
print(matches)


 
