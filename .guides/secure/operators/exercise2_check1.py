import sys

with open('code/operators/exercise2.cpp') as subfile:
  subtext = subfile.read()

  if 'false' in subtext:
    sys.exit(1)  
  elif 'true' in subtext:
    sys.exit(1)

sys.exit(0)