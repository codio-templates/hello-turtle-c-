import sys

with open('code/loops/exercise2.cpp') as subfile:
  subtext = subfile.read()
  
  forloop = subtext.count("for")
  
  whileloop = subtext.count("while")
  
  cout = subtext.count("cout")

  if ((forloop < 1) and (whileloop < 1)):
    print("You did not include either a for or while loop!")
    sys.exit(1)
  if cout != 1:
    print("You need to include ONE and ONLY ONE cout statement!")
    sys.exit(1)
    
sys.exit(0)