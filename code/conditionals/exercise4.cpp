#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char** argv) {
  
  string x = argv[1];
  
  //add code below this line

  int num;
  if (x == "red") {
    num = 1;
  }
  else if (x == "blue") {
    num = 2;
  }
  else if (x == "yellow") {
    num = 3;
  }
  else {
    num = 0;
  }
  
  switch (num) {
    case 1: cout << x + " is a primary color"; break;
    case 2: cout << x + " is a primary color"; break;
    case 3: cout << x + " is a primary color"; break;
    default: cout << x + " is not a primary color";
  }

  //add code above this line
  
  return 0;
  
}
