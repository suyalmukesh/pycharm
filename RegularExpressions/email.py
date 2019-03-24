import re
emails = ['suyalmukesh@gmail.com','suyal@gmail.com','msuyal@gmail.com',
          'suyal.com','suyal@1.2']

regex = re.compile("[\w.%+-]@[\w.-].[a-zA-Z]")

for i in emails:

     if re.search(regex,i):
       print(i,":  Valid match")
     else:
       print(i,": Not valid")