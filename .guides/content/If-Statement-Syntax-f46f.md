---

## If Statement Syntax

Conditionals are pieces of code that make a decision about what the program is going to do next. The most common conditional is the `if` statement.

![.guides/img/IfSyntax](.guides/img/IfSyntax.png)

If statements in C++ must contain the following items:
* The keyword `if`.
* A boolean expression in parentheses, `()`.
* Curly braces, `{}`, surrounding all lines of code that will run if the boolean expression is true.

It is best practice to also indent the lines of code inside the curly braces to visually differentiate them from the commands that will always run. 

Copy the code below into the text editor on the left and then click the `TRY IT` button to see the output. You can also click on the ++Code Visualizer++ link below to see how the program runs behind-the-scenes. If the visualizer does not open properly after a few seconds, click the `Refresh code` code button at the top to restart it.

```c++	
if (5 > 4) {
  cout << "I print 1st if true" << endl;
  cout << "I print 2nd if true" << endl;
}	
cout << "I will always print" << endl;	
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifsyntax.cpp -o code/conditionals/ifsyntax ./code/conditionals/ifsyntax 1)

[Code Visualizer](open_tutor code/conditionals/ifsyntax.cpp)

{Check It!|assessment}(parsons-puzzle-1884977588)
