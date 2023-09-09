# 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
import re
    
pattern = "a.+b$"


input_string = "accddb"
input_string1 = "accddb   annnnd  abbbb"
input_string2 = "accddb"



"aabbbbdb"
"aabAbbbc"

match = re.findall(pattern, input_string1)

print(match)