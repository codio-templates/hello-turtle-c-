---

## If Else Syntax

The if else statement checks to see if a condition is true, and then has specific actions that take place. But it also provides a specific set of actions if the boolean expression is false. Use the `else` keyword to introduce the code to run when false. Notice, `else` is aligned with the `if` keyword (no indentation) and has it's own set of curly braces `{}`. You do not write another boolean expression with `else`.

![.guides/img/if-else-statement-syntax](.guides/img/if-else-statement-syntax.png)

It is best practice to indent the lines of code within the curly braces to differentiate them but the indention does not effect how the program runs.

```c++
if (5 > 4) {
    System.out.println("The boolean expression is true");
}
else {
    System.out.println("The boolean expression is false");
}
```

[Code Visualizer](open_tutor code/conditionals/PlaygroundIfElseSyntax.java)

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelsesyntax.cpp -o code/conditionals/ifelsesyntax ./code/conditionals/ifelsesyntax 1)

|||challenge
## What happens if you:
* Change `4` to `6`?
* Remove all the curly braces `{}`?
* Try to have 2 lines of code run when false without curly braces `{}`?
* Try to have 2 lines of code run when true without curly braces `{}`?

|||

[Code Visualizer](open_tutor code/conditionals/PlaygroundIfElseSyntax.java)

{Try it}(sh .guides/bg.sh g++ code/conditionals/ifelsesyntax.cpp -o code/conditionals/ifelsesyntax ./code/conditionals/ifelsesyntax 2)

{Check It!|assessment}(multiple-choice-88978139)
