---

## Initializing & Assigning Values

We call the process of setting the **initial** value of a variable **initialization**. Recall that you can do this separately after the declaration or combine it into the same statement as the declaration.

![.guides/img/VariableAssignmentInt](.guides/img/VariableAssignmentInt.png)

Since the value stored in a variable can change, we call changing the value **assigning** or **re-assigning**. Use the assignment operator, `=`, to give a variable a new value.

## Accessing Variables

Enter the code below and `TRY IT` to see the results of the `cout` commands. Click on the ++Code Visualizer++ link to see how the value of `my_int` changes.

```c++
int my_int = 123;
cout << my_int << endl;
my_int = 321;
cout << my_int << endl;
```

When we use a variable's name to get the value like in the `cout` statements above, we say we are **accessing** the variable.

{Try it}(sh .guides/bg.sh g++ code/fundamentals/variableval.cpp -o code/fundamentals/variableval ./code/fundamentals/variableval 1)

[Code Visualizer](open_tutor code/fundamentals/variableval.cpp)

{Check It!|assessment}(parsons-puzzle-2436518807)
