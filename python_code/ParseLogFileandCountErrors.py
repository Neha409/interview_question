

import sys


file = sys.argv[1]
errorCounter = 0
warnCounter = 0
infoCounter = 0 
with open(file,'r')as file:
    for line in file.readlines():
      if line.__contains__("ERROR"):
         errorCounter = errorCounter + 1
      elif line.__contains__("WARN"):
         warnCounter = warnCounter + 1
      else:
         infoCounter = infoCounter + 1

print(f"Count of ERROR lines is {errorCounter}")
print(f"Count of WARN lines is {warnCounter}")
print(f"Count of INFO lines is {infoCounter}")