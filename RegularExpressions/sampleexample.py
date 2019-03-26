import re

examplestring = '''
Jessica is 55 years old and Deneial is just 20.
Edward is 97 and his grandfather,Oscar is 102.
'''
ages = re.findall(r'\d{1,3}',examplestring)
names = re.findall(r'[A-Z][a-z]*',examplestring)

print(ages)
print(names)

agedict = {}
x =0
for eachname in names:
    agedict[eachname] = ages[x]
    x+=1

print(agedict)