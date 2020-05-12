---

## Tutorial Lab 3: Fundamentals Challenge

In the code to the left, we see that there are a series of declared and initialized variables. Use these variables along with the `cout <<` and `<< endl;` commands to print out a custom message to customers who open a chat client.

Your output should look something like this:
```c++
Hello! Today is Wednesday, May 4.
The current wait time is 4 minutes.
```

The pattern is as follows. The `*` indicates variables:
```c++
*greeting* Today is *dayOfWeek*, *month* *day*.
The current wait time is *currentWaitMinutes* minutes.
```

To test the code, first click on the `COMPILE` button. This will compile your code and turn it into a program. If your program compiled successfully, you will see the message `Command was successfully executed.` Then you can run your program by clicking on the `TEST` buttons. You will see the output of a few different test cases:

{Compile}(g++ code/fundamentals/labchallenge.cpp -o code/fundamentals/labchallenge)
{Test 1}(sh .guides/run.sh Hello! Monday July 4 9)
{Test 2}(sh .guides/run.sh Howdy! Tuesday December 15 2)
{Test 3}(sh .guides/run.sh Greetings! Friday March 13 39)

Take a look at the test outputs above. Do they look like the expected outputs below? If not, your code may need some revision.
```c++
Hello! Today is Monday, July 4.
The current wait time is 9 minutes.
```
```c++
Howdy! Today is Tuesday, December 15.
The current wait time is 2 minutes.
```
```c++
Greetings! Today is Friday, March 13.
The current wait time is 39 minutes.
```

{Check It!|assessment}(code-output-compare-2157437958)
