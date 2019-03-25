"""
4
bcdef
abcdefg
bcde
bcdef
"""
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

lst = []
n = int(input())
for i in range(n):
    lst.append(input())
sec = unique(lst)

print(len(sec))
for i in sec:
    print(lst.count(i),end =' ')

# Running fine but giving Timeout Error for some test cases in hackerRank
