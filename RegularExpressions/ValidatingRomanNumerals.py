"""Validating Roman Numerals
You are given a string, and you have to validate whether it's a valid
Roman numeral. If it is valid, print True. Otherwise, print False.
Try to create a regular expression for a valid Roman numeral.
Input Format :
A single line of input containing a string of Roman characters.
Output Format :
Output a single line containing True or False according to the instructions above.
"""

# NOT REQUIRED THOUGH BUT WROTE JUST FOR REFERENCE
Roman_dict = {  # Roman Letters for Reference
            'M' : '1000',
            'CM': '900',
            'D' : '500',
            'CD': '400',
            'C' : '100',
            'XC': '90',
            'L' : '50',
            'X' : '10',
            'IX': '9',
            'V' : '5',
            'IV': '4',
            'I' : '1'
           }

import re
in_string = input()

if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", in_string):
    print("True")
else:
    print("False")

# THIS IS VERY TOUGH , THE REGEX TO CREATE 