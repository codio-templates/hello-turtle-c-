---

## If Else Statement

The `if-else` statement is used when you want something *specific* to happen if the boolean expression is true and something *else* to happen if it is false. 

```c++
bool my_bool = true;

if (my_bool) {
  cout << "The value of my_bool is true" <<endl; }
else {
  cout << "The value of my_bool is false" <<endl; }
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelse.cpp -o code/conditionals/ifelse ./code/conditionals/ifelse 1)

|||challenge
## What happens if you:
* Assign `my_bool` to `false`?
* Assign `my_bool` to `! true && ! false`?

|||

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelse.cpp -o code/conditionals/ifelse ./code/conditionals/ifelse 2)

|||important
## IMPORTANT
Did you notice that the code above has the closing curly brace `}` after the the semi-colon `;` instead of on the next line? Curly braces `{}` are required for an `if-else` statement to work, however, the decision of where to place them is entirely up to you. All of the commands below work exactly the same way:
```c++
if (is_true) {
  cout << "Print me!" << endl;
}
```
```c++
if (is_true) {
  cout << "Print me!" << endl; }
```
```c++
if (is_true) { cout << "Print me!" << endl; }
```
|||

## Testing Multiple Cases

You will find yourself needing to test the same variable multiple times. To simplify this, you can **nest** `if-else` statements -- which means you can put an `if-else` structure inside of another `if-else` structure (as shown on the right below). 

![.guides/img/NestedElseIf](.guides/img/NestedElseIf.png)

When nesting `if` and `else` **together**, use the keywords `else` and `if` side-by-side (`else if`). This nesting drastically changes the way the program flows once the correct case is found. On the left, the program checks *every* case no matter the value of the variable. On the right, the **nested** structure causes the program to jump out of the structure once the correct case is found. This is able to occur because the other `if` cases are inside the `else` statement, which will only run when the previous boolean expression is false.

```c++
int grade = 62;
if (grade < 60) {
  cout << "F" << endl; }
else if (grade < 70) {
  cout << "D" << endl; }
else if (grade < 80) {
  cout << "C" << endl; }
else if (grade < 90) {
  cout << "B" << endl; }
else if (grade <= 100) {
  cout << "A" << endl; }
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelse.cpp -o code/conditionals/ifelse ./code/conditionals/ifelse 9)

[Code Visualizer](open_tutor code/conditionals/ifelse.cpp)

{Check It!|assessment}(parsons-puzzle-2567094564)
