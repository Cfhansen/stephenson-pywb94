###solution to exercise 94 from ben stephenson's "the python workbook".

import random

def password():
  length = random.randint(7,10)
  result = ''
  for i in range(length):
    result = result + chr(random.randint(33,126))
  return result

print(password())
