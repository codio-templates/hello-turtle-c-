import sys

with open('code/loops/exercise4.cpp') as subfile:
  subtext = subfile.read()
  
  if subtext.count('for (int i = 100; i <= 100; i--) {') !=1 or \
  subtext.count('if (i == 0) {') !=1 or \
  subtext.count('cout << "Print me!" << endl;') !=1 or \
  subtext.count('else {') !=1 or \
  subtext.count('while (true) {') !=1 or \
  subtext.count('i++;') !=1 or \
  subtext.count('cout << "Don\'t print me!" << endl;') !=1:
    print("You cannot make any changes to the existing code!")
    sys.exit(1)

  if subtext.count('break') != 2:
    print("You must include two and ONLY two break statement!")
    sys.exit(1)
    
sys.exit(0)