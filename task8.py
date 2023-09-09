# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

text = "The quick Brown fox Jumps over 42 Lazy D_ogs H2323."


# The key difference is that [A-Z]\w+ matches any word that starts with an uppercase letter and may contain digits or underscores, while [A-Z][a-z]+ specifically matches words that start with an uppercase letter and are followed by lowercase letters only.

# Using [A-Z]\w+
pattern1 = '[A-Z]\w+'
matches1 = re.findall(pattern1, text)

# Using [A-Z][a-z]+
pattern2 = '[A-Z][a-z]+'
matches2 = re.findall(pattern2, text)

print("Matches using [A-Z]\\w+:", matches1)
print("Matches using [A-Z][a-z]+:", matches2)


 
