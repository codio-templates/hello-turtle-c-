import sys

with open('code/loops/exercise1.cpp') as subfile:
  subtext = subfile.read()
  
  forloop = subtext.count("for")
  
  inti1 = subtext.count("int i = 0 ;")
  inti2 = subtext.count("int i= 0 ;")
  inti3 = subtext.count("int i =0 ;")
  inti4 = subtext.count("int i = 0;")
  inti5 = subtext.count("int i=0 ;")
  inti6 = subtext.count("int i =0;")
  inti7 = subtext.count("int i= 0;")
  inti8 = subtext.count("int i=0;")
  
  tinaforward = subtext.count("tina.forward(100)")
  
  tinaturn = subtext.count("tina.left(120)")

  if forloop < 1:
    print("You did not use a for loop in your code.")
    sys.exit(1)
  if (inti1 or inti2 or inti3 or inti4 or inti5 or inti6 or inti7 or inti8) < 1:
    print("You did use an iterating variable i and/or did not set i to zero.")
    sys.exit(1)
  if tinaforward < 1:
    print("It appears you did not direct tina's path correctly.")
    sys.exit(1)
  if tinaturn < 1:
    print("It appears you did not direct tina's path correctly.")
    sys.exit(1)
    
sys.exit(0)