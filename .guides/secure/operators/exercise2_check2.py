import sys

with open('code/operators/exercise2.cpp') as subfile:
  subtext = subfile.read()

  if 'bool ' in subtext:
    sys.exit(1)

sys.exit(0)