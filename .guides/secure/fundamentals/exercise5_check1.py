import sys

with open('code/fundamentals/exercise5.cpp') as subfile:
  subtext = subfile.read()
  
  if subtext.count('cout') == 2:
    sys.exit(0)
  else:
    sys.exit(1)
