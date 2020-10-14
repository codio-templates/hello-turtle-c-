import sys

with open('code/loops/labchallenge.cpp') as subfile:
  subtext = subfile.read()
  
  forloop = subtext.count("for")
  
  # accounts for int main()
  intcount = subtext.count("int") - 1
  
  cout = subtext.count("cout")

  if forloop < 2:
    print("Please incorporate at least two for loops!")
    sys.exit(1)
  if intcount < 2:
    print("You did not use for loops correctly. Check your code and try again.")
    sys.exit(1)
  if cout > 2:
    print("You are only allowed to use, at most, two cout statements!")
    sys.exit(1)
    
sys.exit(0)