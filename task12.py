# 12. Write a Python program that matches a word containing 'z'.

import re
# 1-soltion:
    # "[A-Z]?[a-z]*z[a-z]*": This pattern explicitly uses character classes [A-Z] and [a-z] to match uppercase and lowercase letters, respectively. It also allows for an optional uppercase letter at the beginning and zero or more lowercase letters before and after 'z'.

#2- solution 
    # allow for any characters in words, including digits and underscore

pattern = "[A-Z]?[a-z]*z[a-z]*"
pattern1="\w*z\w*"

# Input strings
input_string1 = "This is a test."
input_string2 = "The Zebra is fast."
input_string3 = "I love pizza with extra cheese."
input_string4 = "TThe zebra is sleeping."
input_string5 = "A z12Eppelin flew by12333."

match1 = re.search(pattern, input_string1)
match2 = re.search(pattern, input_string2)
match3 = re.search(pattern, input_string3)
match4 = re.search(pattern, input_string4)
match5 = re.search(pattern, input_string5)

print(match1)
print(match2)
print(match3)
print(match4)
print(match5)
