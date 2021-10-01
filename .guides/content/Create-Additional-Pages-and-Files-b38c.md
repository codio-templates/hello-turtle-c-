---

Instruction through Codio is built around the guides feature. This is a brief description on how the demo on the previous page was built. Please see the [**documentation**](https://docs.codio.com/authoring.html) for more information about content authoring with guides.

### Build on this Starter Pack
---
Please note that there are softwares, files, scripts, etc. preconfigured in this **Hello Turtle in C++** Starter Pack that allow for use of turtle in C++. 

* `turtle.sh` file is a Bash script that allows for efficient operations on multiple files in the command line. 
* `CImg.h` and `CTurtle.hpp` are called in the code editor to enable use of the Turtle Graphics library as well as the C Image library. 

Follow the directions below to build out this project with your own activities in turtle:

### Code Editor File
---
Add a `.cpp` file to this project. This should live in the `code` folder in the filetree. This is the file students will edit. Select `New File...` and then type its name and file extension. Copy and paste the following template code into the new file. It is required for turtle to run in C++.

```
////////// DO NOT EDIT HEADER! //////////
#include <iostream>                    //
#include "CTurtle.hpp"                 //
#include "CImg.h"                      //
using namespace cturtle;               //
using namespace std;                   //
/////////////////////////////////////////

int main(int argc, char** argv) {
  
  //add code below this line


  //add code above this line
  
  return 0;
  
}
```

### Page Layout
---
Each page in the guide can have its own layout. You can select how many panels you want, and what information goes in each panel. Click the wrench in the top-right corner of your guide. You can select the layout from here. 

When setting up Turtle Graphics, set the code editor file in panel 0, and the server in panel 1. The guide will be in panel 2. 

![Panels](.guides/img/panelcpp.png)

### Try It Button
---
|||
Use the following markdown syntax when creating the `Try It` button:

```markdown
{Try it|terminal}(bash .guides/turtle.sh g++ filename.cpp -o filename ./filename)
```
|||

Below is an image highlighting what happens after the `TRY IT` button is clicked.

![Try It Button Process](.guides/img/TurtleGraphicsFlow.png)

1. `TRY IT` button is clicked by the user.
2. The `Terminal` tab is opened.
3. The terminal runs the command to compile the program and to display the graphical output.
4. The output is displayed as a screen on the bottom left panel. You can click the screen to close the output.
5. Click on the `turtleloop.cpp` tab to go back to the text editor if you want to make changes to the program.

### Add this Project to a Course
---
You can add this project as an assignment to an existing course:

1. In the course module, click **Add Assignment**.
2. On the Create Assignment page, click **Project based**.
3. To import a project, click the **Click here** link under **Starting Point.** 
4. Click **Copy Project** and browse to the project and select it.
5. Click **Create.**
