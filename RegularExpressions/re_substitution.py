"""
The re.sub() tool (sub stands for substitution) evaluates a pattern and,
for each valid match,it calls a method (or lambda).
The method is called for all matches and can be used to modify strings
in different ways.The re.sub() method returns the modified string as an output.
"""
import re
n = int(input())  # no of lines
line = []
for i in range(n):
    line.append(input())

for i in line:
      i = (re.sub(r"\s[&]{2}\s",' and ',(re.sub(r"\s[|]{2}\s",' or ',i))))
      print(re.sub(r"\s[&]{2}\s",' and ',(re.sub(r"\s[|]{2}\s",' or ',i))))

  # I am doing the substitute operation twice for the consecutive replace
  # like && && && or && && || ||
  # In a single statement replacing twice one for and other for or   

