# The Captain's Room
# Using the collections class here
from collections import Counter
k = int(input())
rooms = input().split()
count=Counter(rooms)
print(count.keys())
for i in count.values():
    if i == 1:
        print(count.keys())
