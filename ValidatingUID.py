"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:
It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits ( 0-9 ).
It should only contain alphanumeric characters (a-z ,A-Z  & 0-9  ).
No character should repeat.
There must be exactly  10 characters in a valid UID.
"""
def dis(a):
    lst = []
    for i in a:
        lst.append(i)
    return len(set(lst))


no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    uid = input()
    UPPER_COUNT,DIGIT_COUNT = 0,0

    if dis(uid) < 10 or dis(uid) > 10 or len(uid) > 10 or not uid.isalnum():
        print('Invalid')

    else:
        for i in uid:
           if i.isupper():
              UPPER_COUNT += 1
           if i.isdigit():
              DIGIT_COUNT += 1
        if UPPER_COUNT < 2 or DIGIT_COUNT < 3:
            print('Invalid')
        else:
            print('Valid')
