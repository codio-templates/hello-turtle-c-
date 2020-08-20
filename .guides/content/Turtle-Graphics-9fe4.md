---

Before continuing with loops, we are going to learn how to create graphical output with the **Turtle Graphics** library. Like a pencil on paper, the turtle object leaves a line as it moves around the screen.

## Turtle Syntax
The first step is to create a **screen** for the turtle to move around in using the command `TurtleScreen` followed by a variable name to call that screen (i.e. `screen`). In parentheses after `screen`, you can specify the dimensions of the screen in terms of **width** and **height** respectively (i.e. `400, 300`). Then we can create our **turtle** using the command `Turtle` followed by a variable name for that turtle (i.e. `tina`). Finally in parentheses, we put in `screen` to associate the turtle with the screen that we created previously. The code below produces a turtle and a screen for the turtle to move around in.

```c++

TurtleScreen screen(400, 300); //width 400 pixels and height 300 pixels
Turtle tina(screen); //creates a turtle named tina inside the screen

```

|||important
### IMPORTANT
You may have noticed that there are additional lines of code within the file in the text editor to your left. It is very **IMPORTANT** that you **DO NOT** edit the header as that will cause the program to run incorrectly.
```c++
#include <iostream>
#include "CTurtle.hpp"
#include "CImg.h"
using namespace cturtle;
using namespace std;
```
The header above enables you to use the Turtle Graphics library as well as the C Image library. Thus, the header should never be altered.
|||

## Turtle Commands
In order to view the turtle object, it is not enough just to create it. You must give instructions to the turtle object in order for it to "move" around the screen. Here is a list of basic turtle commands that you can give to `tina` the turtle object:

|Command|Parameter|Description|
|:-----:|:-------:|:---------:|
|`tina.forward(n)`|Where `n` represents the number of pixels|Move the turtle forward|
|`tina.backward(n)`|Where `n` represents the number of pixels|Move the turtle backward|
|`tina.right(d)`|Where `d` represents the number of degrees|Turn the turtle to the right|
|`tina.left(d)`|Where `d` represents the number of degrees|Turn the turtle to the left|

Let's try this very simple command below. Copy it into the text editor on your left and then click the `TRY IT` button to see the graphical output.

```c++
TurtleScreen screen(400, 300);
Turtle tina(screen);
tina.forward(100);
screen.exitonclick();
```

{Try it|terminal}(bash .guides/turtle.sh g++ turtleloop.cpp -o turtleloop ./turtleloop)

### What does the `screen.exitonclick()` command do?
By default, the screen will close itself automatically once the program reaches the end of the code. However, if you want the screen to remain open, you can use `screen.exitonclick()` to tell the program to keep the screen open until the screen is clicked with a cursor. Go ahead and try clicking on the screen.

## Turtle Output
Below is an image highlighting what happens after the `TRY IT` button is clicked.

![.guides/img/TurtleGraphicsFlow](.guides/img/TurtleGraphicsFlow.png)

1. `TRY IT` button is clicked by the user.
2. The `Terminal` tab is opened.
3. The terminal runs the command to compile the program and to display the graphical output.
4. The output is displayed as a screen on the bottom left panel. You can click the screen to close the output.
5. Click on the `turtleloop.cpp` tab to go back to the text editor if you want to make changes to the program.

{Check It!|assessment}(multiple-choice-1332761997)
