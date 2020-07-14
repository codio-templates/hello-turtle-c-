import sys

with open('code/operators/exercise1.cpp') as subfile:
  subtext = subfile.read()
  
  if 'cout << (a * 3 + b - 8 / 2) << endl;' in subtext:
    sys.exit(0)  
  else:
    sys.exit(1)