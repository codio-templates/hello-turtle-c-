import sys

with open('code/operators/labchallenge.cpp') as subfile:
  subtext = subfile.read()
  
  equality = subtext.count("==") + subtext.count("!=")
  
  #takes into account the "<" and ">" within include <iostream> header and "<<" needed after cout
  lessThan = subtext.count("<") + subtext.count("<=") - (subtext.count("<<")*2) - 1
  greaterThan = subtext.count(">") + subtext.count(">=") - 1
  
  #"!" and "!=" should be counted separately
  logical = subtext.count("&&") + subtext.count("||") + subtext.count("!") - subtext.count("!=")

  if equality < 1:
    print("Please incorporate at least one equality operator.")
    sys.exit(1)
  if lessThan < 1:
    print("Please incorporate at least one less than operator.")
    sys.exit(1)
  if greaterThan < 1:
    print("Please incorporate at least one greater than operator.")
    sys.exit(1)
  if logical < 2:
    print("Please incorporate at least two logical operators.")
    sys.exit(1)

sys.exit(0)