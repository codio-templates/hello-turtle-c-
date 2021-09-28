////////// DO NOT EDIT HEADER! //////////
#include <iostream>                    //
#include "CTurtle.hpp"                 //
#include "CImg.h"                      //
using namespace cturtle;               //
using namespace std;                   //
/////////////////////////////////////////

int main(int argc, char** argv) {
  
  //add code below this line

TurtleScreen screen(400, 300);
Turtle tina(screen);
tina.forward(100);
screen.exitonclick();

  //add code above this line
  
  return 0;
  
}
