---

## Swith Case Statement Syntax

The `switch case` statement is a way to make a decision with multiple possible outcomes. Instead of nesting or sequencing many `if` statements, C++ allows you to write the following:

![.guides/img/SwitchCase](.guides/img/SwitchCase.png)

Here are the rules for writing a switch case statement:

* Start with `switch` followed by the variable that is going to be tested in parentheses `()`.
* All of the `case`s are surrounded by a set curly braces `{}`.
* Each `case` is followed by a value (numeric or string) and a colon `:`.
* After each `:`, write the code that should run if the variable is equal to that case's value.
* After each section of code per case, include `break;`.
* As the very last case, use `default:` to specify what should happen if none of the above cases are true.

```c++
int dayOfWeek = 3;

switch (dayOfWeek) {

  case 1: cout << "Sunday"; //only prints if dayOfWeek == 1
          break;
  case 2: cout << "Monday"; //only prints if dayOfWeek == 2
          break;
  case 3: cout << "Tuesday"; //only prints if dayOfWeek == 3
          break;
  case 4: cout << "Wednesday"; //only prints if dayOfWeek == 4
          break;
  case 5: cout << "Thursday"; //only prints if dayOfWeek == 5
          break;
  case 6: cout << "Friday"; //only prints if dayOfWeek == 6
          break;
  case 7: cout << "Saturday"; //only prints if dayOfWeek == 7
          break;
  default: cout << "Invalid"; //only prints if none of the above are true
    
}
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/switchsyntax.cpp -o code/conditionals/switchsyntax ./code/conditionals/switchsyntax 1)

[Code Visualizer](open_tutor code/conditionals/switchsyntax.cpp)

|||challenge
## What happens if you:
* Assign `dayOfWeek` to `5`?
* Assign `dayOfWeek` to `0`?
* Assign `dayOfWeek` to `3` and remove all of the `break;` statements?

|||

{Try it}(sh .guides/bg.sh g++ code/conditionals/switchsyntax.cpp -o code/conditionals/switchsyntax ./code/conditionals/switchsyntax 2)

[Code Visualizer](open_tutor code/conditionals/switchsyntax.cpp)

{Check It!|assessment}(multiple-choice-2585797860)
