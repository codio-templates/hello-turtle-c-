---

Complete the code on the left such that the code returns `17`. Please note there are *two* types of errors present in the code:

1) A **compilation error** - the compiler sees a problem and throws an error to alert you.

2) A **run-time error** - an error when the code is running.

<details><summary><b>Compilation Error Hint</b></summary>An example of a compilation error would be <code>int number = "this is not an int";</code></details>

{Try it}(sh .guides/bg.sh g++ code/operators/exercise1.cpp -o code/operators/exercise1 ./code/operators/exercise1 1)

{Check It!|assessment}(test-1204552917)

|||info
## How to Restore Code File
If you make too many changes to the code on the left and want to start over, click on the gear in the top-right and select `Restore current files`. ![.guides/img/Restore](.guides/img/Restore.png)
|||

<details><summary><b>Run-Time Error Hint</b></summary>Once you fix the compilation error, you will see that the code output does not match what the exercise asks for.</details>

<details><summary><b>Try Debugging</b></summary>Debugging is a set of practices used to remove bugs (defects or flaws within a program). One way is to print out useful information. Try printing out what the variables <i>should</i> be to get to <b>17</b>: <br> $a = 17 - \frac{b-8/2}{3}$ <br> $b = 17 - a * 3 + \frac{8}{2}$ <br> <br> You can also try tweaking the variables to see how that changes the output of the code. For example, what happens when you try assigning <code>a</code> to <code>6</code> instead of <code>5</code>?</details>

{Try it}(sh .guides/bg.sh g++ code/operators/exercise1.cpp -o code/operators/exercise1 ./code/operators/exercise1 2)

{Check It!|assessment}(test-951636893)
