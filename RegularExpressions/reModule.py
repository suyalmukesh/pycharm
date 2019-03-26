"""
https://www.youtube.com/watch?v=K8L6KVGG-7o
"""
import re

senetence = "Start a sentence abd bring to en end "

pattern = re.compile(r'sen')

matches = pattern.finditer(senetence)

for match in matches:
    print(match)

# keep adding to this program...will be a single reference