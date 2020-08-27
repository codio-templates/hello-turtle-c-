////////// DO NOT EDIT HEADER! //////////
#include <iostream>                    //
#include "CTurtle.hpp"                 //
#include "CImg.h"                      //
using namespace cturtle;               //
using namespace std;                   //
/////////////////////////////////////////

int main(int argc, char** argv) {
  
  TurtleScreen screen(400, 300); //You may edit the dimensions to fit your window
  Turtle tina(screen);
  tina.speed(TS_SLOWEST);
  
  //add code below this line

for (int x = 0; x < 3; x++) {
  tina.back(100);
  tina.right(120);
}

  //add code above this line
  
  screen.exitonclick();
  return 0;
  
}
