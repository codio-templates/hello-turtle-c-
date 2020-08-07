---

## Infinite Loops Are Bad, Right?
Well, that depends. If an infinite loop is caused because the counting variable isn't incremented, then it's a bug. However, some programmers purposely create a condition that will always evaluate to true. Therefore, the loop will always run. In such cases, a `break` statement is used to stop the loop at a particular point in the program.

Take a look at the code to the left in the text editor. Then click on the `TRY IT` button below several times to run the code and see the resulting outputs. You can also click on the ++Code Visualizer++ link below to see how the code runs behind-the-scenes.

{Try it}(sh .guides/bg.sh g++ code/loops/breakstatement.cpp -o code/loops/breakstatement ./code/loops/breakstatement 1)

[Code Visualizer](open_tutor code/loops/breakstatement.cpp)

Even though `while (true)` will always evaluate as a true statement, the loop never becomes infinite because of the `break` statement.

|||challenge
## What happens if you:
* Remove `break;` from the program?
* Add `break;` to the line before `cout << "The loop ends" << endl;`?

|||

{Try it}(sh .guides/bg.sh g++ code/loops/breakstatement.cpp -o code/loops/breakstatement ./code/loops/breakstatement 2)

[Code Visualizer](open_tutor code/loops/breakstatement.cpp)

### Comparing While Loops
The `while` loops introduced on the previous pages look different from the `while` loop covered on this page; however, they both have the same components and behave similarly.

![.guides/img/WhileLoopComparison](.guides/img/WhileLoopComparison.png)

{Check It!|assessment}(multiple-choice-1083783003)
