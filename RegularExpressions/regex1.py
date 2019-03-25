"""
Sample Input rabcdeefgyYhFjkIoomnpOeorteeeeet
Output :
ee
Ioo
Oeo
eeeee
"""
import re

#input_string = input()
# MyVersion
input_string = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
regex = re.compile("[^aeiouAEIOU]?[aeiouAEIOU]{2,}[^aeiouAEIOU]?")
a = re.findall(regex,input_string)
print(a)

# ----------------------------------------------

""" Hacker Rank Version """
vowels ="aeiou"
consonants = "^aeiou"
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)

print(match)

"""
(?<=[expression])[pattern]  #positive lookbehind
(?<![expression])[pattern]  #negative lookbehind

"""

# -------------------------------------------

import re

VOWELS = '[aeiou]'
CONSONANTS = '[^aeiou]'
REGEX = '(?<=' + CONSONANTS +')(' + VOWELS + '{2,})' + CONSONANTS

match = re.findall(REGEX, input(), re.I)
print('\n'.join(match or ['-1']))