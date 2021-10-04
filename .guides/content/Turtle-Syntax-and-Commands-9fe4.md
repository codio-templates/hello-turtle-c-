---
Turtle Graphics allows students to create graphical output with the Turtle Graphics library. Like a pencil on paper, the Turtle object leaves a line as it moves around the screen.

![Turtle C++ GIF](.guides/img/TurtleExercise1.gif)

### Turtle Syntax
---
The first step is to create a **screen** for the turtle to move around in using the command `TurtleScreen` followed by a variable name to call that screen (i.e. `screen`). In parentheses after `screen`, you can specify the dimensions of the screen in terms of **width** and **height** respectively (i.e. `400, 300`). Then we can create our **turtle** using the command `Turtle` followed by a variable name for that turtle (i.e. `tina`). Finally in parentheses, we put in `screen` to associate the turtle with the screen that we created previously. The code below produces a turtle and a screen for the turtle to move around in. 

```c++

	TurtleScreen screen(400, 300); //width 400 pixels by height 300 pixels
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

### Turtle Commands
---
In order to view the turtle object, it is not enough just to create it. You must give instructions to the turtle object in order for it to "move" around the screen. Here is a list of basic turtle commands that you can give to `tina` the turtle object:

|Command|Parameter|Description|
|:-----:|:-------:|:---------:|
|`tina.forward(n)`|Where `n` represents the number of pixels|Move the turtle forward|
|`tina.backward(n)`|Where `n` represents the number of pixels|Move the turtle backward|
|`tina.right(d)`|Where `d` represents the number of degrees|Turn the turtle to the right|
|`tina.left(d)`|Where `d` represents the number of degrees|Turn the turtle to the left|

++**Sample Code:**++ Let's try this very simple command below. **Copy and paste** the following code in the editor on the left. C++ style guidelines call for indentation with four spaces. Click the `TRY IT` button to see the graphical output.

```c++
	TurtleScreen screen(400, 300);
	Turtle tina(screen);
	tina.forward(100);
	screen.exitonclick();
```

{Try it|terminal}(bash .guides/turtle.sh g++ turtleloop.cpp -o turtleloop ./turtleloop)

++**Important Note:**++
Be sure to exit out of the terminal and turtle preview window between runs of the `Try it` button. This will update the preview window and allow any changes in your code to be reflected accurately in the turtle's movements.

<details><summary> <b>What does the <code>screen.exitonclick()</code> command do?</b></summary> By default, the screen will close itself automatically once the program reaches the end of the code. However, if you want the screen to remain open, you can use <code>screen.exitonclick()</code> to tell the program to keep the screen open until the screen is clicked with a cursor. Go ahead and try clicking on the screen.</details><br>

### Customize Your Turtle
---
You may choose to change the dimensions of your turtle screen whenever you'd like. Also, the following table provides additional commands you can use to customize `tina` the turtle.

|Command|Parameter|Examples|
|:-----:|:-------:|:---------:|
|`tina.pencolor({"COLOR"})`|Where `COLOR` represents the track or line color you want tina to leave behind|red, orange, yellow, green, blue, purple|
|`tina.width(W)`|Where `W` represents how wide (in pixels) tina's track is|any positive integer (e.g. 1, 10, 123, etc.)|
|`tina.shape("SHAPE")`|Where `SHAPE` represents the shape tina takes|triangle, indented triangle, square, arrow|
|`tina.speed(SPEED)`|Where `SPEED` represents how fast tina moves|TS_FASTEST, TS_FAST, TS_NORMAL, TS_SLOW, TS_SLOWEST|

|||info
### NOTE
Due to the dynamic and graphical nature of the Turtle Graphics library, **jagged** lines and **spotty** pixels may appear randomly as the output is being drawn. This is completely **normal**!
|||
