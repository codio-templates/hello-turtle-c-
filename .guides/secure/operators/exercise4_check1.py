import sys

with open('code/operators/exercise4.cpp') as subfile:
  subtext = subfile.read()

  if subtext.count('cout') != 1:
    print("Make sure you are using only 1 cout statement!")
    sys.exit(1) 
    
  if subtext.count("=") != 2:
    print("Make sure you are declaring and assigning two variables.")
    sys.exit(1)
    
  if subtext.count('printf') > 0:
    print("You should not be using printf() in your code!")
    sys.exit(1)
    
sys.exit(0)