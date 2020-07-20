---

## If Statement

`if` statements test to see if a certain condition is true. If yes, then specific commands are run. The simple `if` statement does not do anything if the boolean expression is false.

```c++
if (7 != 10) {
    cout << "The above statement is true" << endl;
    cout << "The above statement is still true" << endl;
}
cout << "This is not related to the if statement" << endl;
```

{Try it}(sh .guides/bg.sh g++ code/conditionals/if.cpp -o code/conditionals/if ./code/conditionals/if 1)

[Code Visualizer](open_tutor code/conditionals/if.cpp)

|||challenge
## What happens if you:
* Change `!=` in the code above to `==`?
* Change `7 != 10` in the code above to `true`?
* Change `7 != 10` in the code above to `false`?
* Remove the curly braces `{}` with the condition set to `if (false)`?

|||

{Try it}(sh .guides/bg.sh g++ code/conditionals/if.cpp -o code/conditionals/if ./code/conditionals/if 2)

[Code Visualizer](open_tutor code/conditionals/if.cpp)

## Testing Multiple Cases

You will find yourself needing to test the same variable multiple times. Be sure that you set up your conditionals to test **all** possible values of the variable.

```c++
int grade = 90;

if (grade > 70) {
    cout << "Congrats, you passed the class" << endl;
}
    
if (grade < 70) {
    cout << "Condolences, you did not pass the class" << endl;
}
```

[Code Visualizer](open_tutor code/conditionals/PlaygroundIf.java)

{Try it}(sh .guides/bg.sh g++ code/conditionals/if.cpp -o code/conditionals/if ./code/conditionals/if 3)

|||challenge
## What happens if you:
* Assign `int grade` to `60`?
* Assign `int grade` to `70`?
* Change `grade > 70` in the code above to `grade >= 70`?

|||

{Try it}(sh .guides/bg.sh g++ code/conditionals/if.cpp -o code/conditionals/if ./code/conditionals/if 4)

[Code Visualizer](open_tutor code/conditionals/if.cpp)

{Check It!|assessment}(multiple-choice-864536125)
