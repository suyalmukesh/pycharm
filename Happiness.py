"""
3 2
1 5 3
3 1
5 7
"""
# Input handling section
n,m    = map(int,input().split())
line_2 = map(int,input().split())
line_3 = map(int,input().split())
line_4 = map(int,input().split())
Happiness = 0
for i in line_2:
    if i in line_3:
        Happiness += 1
    if i in line_4:
        Happiness -+ 1

print(Happiness)


# ------------------------------------------------