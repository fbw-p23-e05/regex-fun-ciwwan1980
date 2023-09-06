#11. Write a Python program that matches a word at the end of a string, with optional punctuation.

import re

pattern = '[A-Z]?[a-z]+\.?$'


print(re.search(pattern, 'Alex.'))  
print(re.search(pattern, 'Or'))     
print(re.search(pattern, 'alex'))   
print(re.search(pattern, 'max.'))   


print(re.search(pattern, 'ABC 123'))  
print(re.search(pattern, 'Alex Sar.'))  
print(re.search(pattern, 'a_/@67b.'))   
