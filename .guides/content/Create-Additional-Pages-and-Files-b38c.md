---

Instruction through Codio is built around the guides feature. This is a brief description on how the demo on the previous page was built. Please see the [documentation](https://docs.codio.com/courses/authoring/) for more information about content authoring with guides.

### Code Editor File
---
Add a `.cpp` file to your project. This should live in the `code` folder. This is the file students will edit. Right-click on the name of your project or book in the directory tree on the left. Select `New File...` and then type its name and file extension. Copy and paste the following template code into the new file. It is required for turtle to run in C++.

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

### Markdown
---
Guides are authored with [markdown](https://docs.codio.com/courses/authoring/#markdown-content-editing), but you can use any HTML to author content. 

### Try It Button
---
|||
Use the following markdown syntax when creating the `Try It` button:

```markdown
{Try it|terminal}(bash .guides/turtle.sh g++ filename.cpp -o filename ./filename)
```
|||

Below is an image highlighting what happens after the `TRY IT` button is clicked.

![.guides/img/TurtleGraphicsFlow](.guides/img/TurtleGraphicsFlow.png)

1. `TRY IT` button is clicked by the user.
2. The `Terminal` tab is opened.
3. The terminal runs the command to compile the program and to display the graphical output.
4. The output is displayed as a screen on the bottom left panel. You can click the screen to close the output.
5. Click on the `turtleloop.cpp` tab to go back to the text editor if you want to make changes to the program.

|||info
### NOTE
Due to the dynamic and graphical nature of the Turtle Graphics library, **jagged** lines and **spotty** pixels may appear randomly as the output is being drawn. This is completely **normal**!
|||
