---

## Boolean
A boolean variable can only take on the value of `true` or `false`. You will see how boolean values are used when we talk about conditionals and while loops. Add the code below and `TRY IT`.

```c++
bool thisIsFun = true;
cout << boolalpha << thisIsFun << endl;
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/boolean.cpp -o code/fundamentals/boolean ./code/fundamentals/boolean 1)

|||challenge
## What happens if you:
* Change the variable to `false`?
* Remove the `boolalpha <<` command?
* Change the variable to `True`?
* Change the variable to `False`?
* Change the variable to `TRUE`?

|||

{Try it}(sh .guides/bg.sh g++ code/fundamentals/boolean.cpp -o code/fundamentals/boolean ./code/fundamentals/boolean 2)

You may have noticed that printing a boolean of `true` resulted in a `1` and a boolean of `false` resulted in a `0` when you remove the `boolalpha <<` command. In C++, the boolean value of `true` is associated with the integer `1` while the boolean value of `false` is associated with the integer `0`. Assigning the value of `True` or `False` to a boolean variable will cause an error message to appear.

{Check It!|assessment}(multiple-choice-3639612203)
