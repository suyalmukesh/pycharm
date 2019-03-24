import re

st = "Hi This is Mukesh , Mukesh is working hard ..I mean really Hard"

regex = re.compile("['Mukesh]")

print(len(re.findall(regex,st)))


