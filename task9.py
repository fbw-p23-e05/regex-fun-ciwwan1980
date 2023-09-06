# 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
import re
    
pattern = "a*b$"


input_string = "accddbbjjj"

"aabbbbdb"
"aabAbbbc"

match = re.search(pattern, input_string)

print(match)