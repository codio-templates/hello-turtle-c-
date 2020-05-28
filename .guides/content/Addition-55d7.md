---

## The Addition (+) Operator
The addition operator works as you would expect with numbers. Copy and paste the code below into the text editor on the left. Make sure your code is in between the `//add code below this line` and `//add code above this line` comments. Then click the `TRY IT` button to see what is outputted by the code.

```c++
cout << 7 + 3;
```

{Try it}(sh .guides/bg.sh g++ code/operators/addition.cpp -o code/operators/addition ./code/operators/addition 1)

You can also add two variables together. Modify the code to look like what's below and then click the `TRY IT` button again.

```c++
int a = 7;
int b = 3;
cout << a + b;
```

{Try it}(sh .guides/bg.sh g++ code/operators/addition.cpp -o code/operators/addition ./code/operators/addition 2)

|||challenge
## What happens if you:
* Make `a` of type double (e.g. `double a = 7.0;`)?
* Change `double a = 7.0` to `double a = 7.1`?
* Make `b` a negative number (e.g. `int b = -3;`)?
* Make `b` an explicitly positive number (e.g. `int b = +3;`)

|||

{Try it}(sh .guides/bg.sh g++ code/operators/addition.cpp -o code/operators/addition ./code/operators/addition 3)

{Check It!|assessment}(multiple-choice-3568628709)

