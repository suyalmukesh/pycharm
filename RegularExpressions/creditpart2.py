"""
CHALLENGING PROBLEM ... TAKINGS A LOT OF TIME : DATED - 28MARCH2019
"""
import re

def Validate_CC(c_no):
    match1 = re.search(r'([456][0-9]{3})-*([0-9]{4})-*([0-9]{4})-*([0-9]{4})', c_no)

    if match1:
           c_no = c_no.replace('-', '')

           ind = 0
           for i in range(0, 16):
              part = c_no[i:i+4]

              if re.search(r'(([\d]{2})\2)+', part):
                  print('part 0',part)
                  ind = 0
                  break
              else:
                print('part 1',part)
                ind = 1
                continue

    else:
        ind = 0
        print('part 0')
    return(ind)

for i in range(int(input())):
    c_no = input()
    if Validate_CC(c_no):
        print("Valid")
    else:
        print("Invalid")