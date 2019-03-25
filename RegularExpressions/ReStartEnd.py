"""
INPUT :
aaadaa
aa
OUTPUT :
(0, 1)
(1, 2)
(4, 5)
"""
import re
s = input()
v = input()
for i,x in enumerate(s):
    if re.match(v,s[i:]):  # searching from every ith next position 
        print((i,i+len(v)-1))
if re.search(v, s)==None:
    print((-1,-1))


