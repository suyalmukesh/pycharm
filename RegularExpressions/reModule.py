"""
https://www.youtube.com/watch?v=K8L6KVGG-7o
"""
import re

senetence = "Start a sentence abd bring to en end"

pattern   = re.compile(r'sen')
pattern2  = re.compile(r'^Start')  # Checking the start string
pattern3  = re.compile(r'end$')    # Checking the end string
pattern4  = re.compile(r'1{4}|2{4}')

matches = pattern4.finditer(senetence)

for match in matches:
    print(match)

# keep adding to this program...will be a single reference