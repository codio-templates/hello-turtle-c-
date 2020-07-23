---

## If Else Syntax

The `if-else` statement checks to see if a condition is true, and then has specific actions that take place. However, it also provides a specific set of actions if the boolean expression is false. Use the `else` keyword to introduce the code to run when false is evaluated. Note that `else` is aligned with the `if` keyword (no indentation) and has its own set of curly braces `{}`. You do *not* write another boolean expression with `else`.

![.guides/img/IfElseSyntax](.guides/img/IfElseSyntax.png)

It is best practice to indent the lines of code within the curly braces to differentiate them but the indention does not affect how the program runs.

```c++
if (5 > 4) {
  cout << "Print me if true" << endl;
}
else {
  cout << "Print me if false" << endl;
}
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelsesyntax.cpp -o code/conditionals/ifelsesyntax ./code/conditionals/ifelsesyntax 1)

[Code Visualizer](open_tutor code/conditionals/ifelsesyntax.cpp)

|||challenge
## What happens if you:
* Change `4` in the code above to `6`?
* Remove all the curly braces `{}`?
* Add another command under `cout << "Print me if true" << endl;` *without* curly braces `{}`?
* Add another command under `cout << "Print me if false" << endl;` *without* curly braces `{}`?

|||

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelsesyntax.cpp -o code/conditionals/ifelsesyntax ./code/conditionals/ifelsesyntax 2)

[Code Visualizer](open_tutor code/conditionals/ifelsesyntax.cpp)

{Check It!|assessment}(multiple-choice-2227929766)
