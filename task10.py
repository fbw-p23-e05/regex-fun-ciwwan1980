# 10. Write a Python program that matches a word at the beginning of a string.

import re

pattern ="^(cat)*"

# Test cases
test_strings = [
    "catsup is delicious",
    "caterpillar is crawling",
    "dog and cat",
    "catch the ball",
    "category",
    "catcat",
    "dogcatcat and the hat"
]

for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"Match found in '{test_string}': {match}")
    else:
        print(f"No match found in '{test_string}'")
