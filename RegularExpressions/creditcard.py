import re

#
def Validate_CC(c_no):
    c_no = c_no.replace('-','')
    print(c_no)
    match1 =  re.search(r'([456][0-9]{3})-*([0-9]{4})-*([0-9]{4})-*([0-9]{4})',c_no)

    if match1:

        for i in range(1,5):
           if re.search(r'(([\d]{2})\2)+',match1.group(i)):
              break
           else:
              continue
        print("Valid")
    else:
        print("Invalid")

for i in range(int(input())):
    c_no = input()
    Validate_CC(c_no)