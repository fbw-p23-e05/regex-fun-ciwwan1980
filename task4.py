# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
# import re

# input_string = "ab"

# pattern = '^ab?$'

# match = re.search(pattern, input_string)

# if match:
#     print("Match found:", match)
# else:
#     print("No match found.")

import re

# Define the regular expression
regex = r'^ab?$'

# Test strings
test_strings = ["ab", "a", "abb", "abc", "cab", "ac", "b", "abbbbb"]

# Check if each string matches the regex pattern
for test_string in test_strings:
    if re.match(regex, test_string):
        print(f'"{test_string}" matches: Yes')
    else:
        print(f'"{test_string}" matches: No')
