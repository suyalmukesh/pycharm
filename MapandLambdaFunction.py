n = int(input())
lst = []
a,b = 0,1
lst.append(0)
lst.append(1)
for i in range(n-2):
     c=a+b
     lst.append(c)
     a,b=b,c

cube = lambda x:x**3
print(list(map(cube,lst)))
