---

## If Statement Syntax

Conditionals are pieces of code that make a decision about what the program is going to do next. The most common conditional is the *if* statement.

![If Statement Syntax](.guides/img/if-statement-syntax.png)


If statements in C++ must contain the following items:
* the keyword `if`
* a boolean expression in parentheses
* curly braces surrounding all lines of code that will run if the boolean expression is true

It is best practice to also indent the lines of code inside the curly braces to visually differentiate them from the commands that will always run.

```c++	
if(5 > 4) {
  System.out.println("1st command if true");
  System.out.println("2nd command if true");
}	
System.out.println("I will always print!");	
```

[Code Visualizer](open_tutor code/conditionals/PlaygroundIfSyntax.java)

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifsyntax.cpp -o code/conditionals/ifsyntax ./code/conditionals/ifsyntax 1)

{Check It!|assessment}(parsons-puzzle-4036047307)
