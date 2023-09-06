#     ^ at the start of a regular expression pattern: It asserts that the pattern must match at the beginning of a line or string. It effectively anchors the pattern to the start.

#     ^ inside a character class (square brackets []): When used inside a character class, like [^abc], it means "negation." It matches any character that is not one of the characters listed within the brackets.

# Here are some examples to illustrate the use of ^ as an anchor:

#     Pattern: ^cat

#         This pattern will match "cat" only if it appears at the very beginning of a line or string.

#         Example: It will match "cat" in "cats are cute," but not in "I have a cat."

#     Pattern: ^[0-9]

#         This pattern will match a digit only if it appears at the beginning of a line or string.

#         Example: It will match "3.14" in "3.14 is a number," but not in "The number is 3.14."

#     Pattern: ^[A-Z]

#         This pattern will match an uppercase letter only if it appears at the beginning of a line or string.

#         Example: It will match "A" in "Alice is here," but not in "The alphabet starts with 'A'."

# In summary, the caret (^) is used as an anchor in regular expressions to specify that a pattern must match at the beginning of a line or string. It helps to control where in the text the pattern should start matching.

import re

print("here start the first case")
pattern = "^cat"


input_string1 = "cats are cute."
input_string2 = "I have a cat."


match1 = re.search(pattern, input_string1)
match2 = re.search(pattern, input_string2)

if match1:
    print(f"Match 1 found: '{match1.group()}'")
else:
    print("Match 1 not found.")

if match2:
    print(f"Match 2 found: '{match2.group()}'")
else:
    print("Match 2 not found.")


print("here start the second case")

pattern = "^[A-Z]"

input_string1 = "Alice is here."
input_string2 = "The alphabet starts with 'A'."


match1 = re.search(pattern, input_string1)
match2 = re.search(pattern, input_string2)

if match1:
    print(f"Match 1 found: '{match1.group()}'")
else:
    print("Match 1 not found.")

if match2:
    print(f"Match 2 found: '{match2.group()}'")
else:
    print("Match 2 not found.")

print("here start the third case")

pattern = "[^abc]"


input_string1 = "apple"
input_string2 = "banana"
input_string3 = "cherry"
input_string4 = "date"


match1 = re.search(pattern, input_string1)
match2 = re.search(pattern, input_string2)
match3 = re.search(pattern, input_string3)
match4 = re.search(pattern, input_string4)

if match1:
    print(f"Match 1 found: '{match1.group()}'")
else:
    print("Match 1 not found.")

if match2:
    print(f"Match 2 found: '{match2.group()}'")
else:
    print("Match 2 not found.")

if match3:
    print(f"Match 3 found: '{match3.group()}'")
else:
    print("Match 3 not found.")

if match4:
    print(f"Match 4 found: '{match4.group()}'")
else:
    print("Match 4 not found.")