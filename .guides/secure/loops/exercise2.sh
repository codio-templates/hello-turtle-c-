#!/bin/sh

g++ code/loops/exercise2.cpp -o code/loops/exercise2

if [ $? -ne 0 ]; then 
  echo "</br><hr/><h3>Your code has compilation errors!</h3>"
  echo "Try correcting the errors listed above."
  exit 1; 
fi

OUTPUT1=("$(./code/loops/exercise2 Testing)")
OUTPUT2=("$(./code/loops/exercise2 Happy)")
OUTPUT3=("$(./code/loops/exercise2 5050)")
OUTPUT4=("$(./code/loops/exercise2 hi+bye)")

if [ -z "$OUTPUT1" ]; then
  echo "<br/><hr/><h3>Challenge Feedback</h3>"
  echo "Your code does not seem to be outputting anything. Make sure you are using: <code>cout</code> and <code>endl;</code> to print the requested pattern."
  exit 1;
fi

if [ "$OUTPUT2" != "Happy
Happy
Happy
Happy
Happy
Happy
Happy
Happy
Happy
Happy" ]; then 
  echo "<br/><hr/><h3>Challenge Feedback</h3>"
  echo "Your code is not printing the requested output correctly."
  exit 1
fi

if [ "$OUTPUT3" != "5050
5050
5050
5050
5050
5050
5050
5050
5050
5050" ]; then 
  echo "<br/><hr/><h3>Challenge Feedback</h3>"
  echo "Your code is not printing the requested output correctly."
  exit 1
fi

if [ "$OUTPUT4" != "hi+bye
hi+bye
hi+bye
hi+bye
hi+bye
hi+bye
hi+bye
hi+bye
hi+bye
hi+bye" ]; then 
  echo "<br/><hr/><h3>Challenge Feedback</h3>"
  echo "Your code is not printing the requested output correctly."
  exit 1
fi

python3 .guides/secure/loops/exercise2_check1.py
if [ $? -ne 0 ]; then 
  echo "</br><hr/><h3>Something is not quite right...</h3>"
  echo "Your output is correct but see the comments above to ensure you are following the assignment guidelines."
  exit 1; 
fi

echo "<h3>Your code is error-free and works as expected!</h3>"
echo "Nice work."
exit 0;