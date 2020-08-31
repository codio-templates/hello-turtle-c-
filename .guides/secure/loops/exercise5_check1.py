import sys

with open('code/loops/exercise5.cpp') as subfile:
  subtext = subfile.read()
  
  forloop = subtext.count("for")
  
  whileloop = subtext.count("while")
  
  loop = forloop + whileloop
  
  cout = subtext.count("cout")
  
  # Prevents use of cout << "." and cout << '.'
  dot1 = subtext.count("\".\"")
  dot2 = subtext.count("\'.\'")
  coutdot = dot1 + dot2
  
  # Prevents use of printing too many periods
  dot = subtext.count(".")
  
  if loop != 2:
    print("You did not include two and only two loops in your code!")
    sys.exit(1)

  if cout != 2:
    print("You did not include two and only two cout statements in your code!")
    sys.exit(1)
    
  if (coutdot >= 10) or (dot >= 10):
    print("You did not satisfy all of the requirements outlined in the assignment.")
    sys.exit(1)

sys.exit(0)