---

## Tutorial Lab 1: If Statements

The `if` statement allows for your program to make a decision about what it should do. It asks a simple question: "Is this condition true?" If yes, then the computer will execute certain commands.

```c++
int x = 5;

if (x < 10) {
  cout << "Less than 10" << endl;
}
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/labifstatement.cpp -o code/conditionals/labifstatement ./code/conditionals/labifstatement 1)

[Code Visualizer](open_tutor code/conditionals/labifstatement.cpp)

An `if` statement is comprised of the keyword `if`, followed by a boolean expression surrounded by parentheses `()`. Any code that should run if the boolean expression is true is surrounded by curly braces `{}`. It is best practice to indent this code, but it does not affect how the code runs.

If the boolean expression is false, the code in curly braces is skipped, and the program continues as normal.

```c++
int x = 20;

if (x < 10) {
  cout << "Less than 10" << endl;
}
    
cout << "And the program continues...";
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/labifstatement.cpp -o code/conditionals/labifstatement ./code/conditionals/labifstatement 2)

[Code Visualizer](open_tutor code/conditionals/labifstatement.cpp)

`if` statements can be used to test multiple conditions. These conditions exist as boolean expressions inside the parentheses `()`. In addition, an `if` statement can exist *inside* another `if` statement. Both blocks of code below accomplish the same exact task.

<table>
<tr>
<td>
<div style="width:245px; height:150px">

```c++
int age = 15;

if (age < 20) {
  if (age > 10) {
    cout << "Teenager";
  }
}
```

</div>
</td>
<td>
<div style="width:310px; height:150px">
          
```c++
int age = 15;

if ((age < 20) && (age > 10)) {
  cout << "Teenager";
}
```

</div>
</td>
</tr>
</table>

{Try it}(sh .guides/bg.sh g++ code/conditionals/labifstatement.cpp -o code/conditionals/labifstatement ./code/conditionals/labifstatement 3)

[Code Visualizer](open_tutor code/conditionals/labifstatement.cpp)

{Check It!|assessment}(multiple-choice-691458048)
