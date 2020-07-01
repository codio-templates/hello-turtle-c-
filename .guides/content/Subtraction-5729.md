---

## Subtraction
Copy the code below and `TRY IT`.

```c++
int a = 10;
int b = 3;
int c = a - b;
cout << c << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/subtraction.cpp -o code/operators/subtraction ./code/operators/subtraction 1)

|||challenge
## What happens if you:
* Assign `b` to `-3`?
* Assign `c` to `a - -b`?
* Assign `b` to `3.1`?
* Change `int b` to `bool b = true;`

|||

|||important
## IMPORTANT
Did you notice that you were able to subtract a `bool` from an `int`? Recall that a `bool` of `true` is actually an integer of `1` and `false` is actually `0`. Thus, the system is able to add and subtract `bool`s and `int`s. In addition, assigning `b` which is of type `int` to `3.1` will force the variable to adopt the integer value of `3` instead. Remember that all `int`s disregard decimal places.

|||

{Try it}(sh .guides/bg.sh g++ code/operators/subtraction.cpp -o code/operators/subtraction ./code/operators/subtraction 2)

## The `--` and `-=` Operators
Decrementing is the opposite of incrementing. Just like you can increment with `++`, you can decrement using `--`.

```c++
int a = 10;
a--;
cout << a << endl;
```

Like `+=`, there is a shorthand for decrementing a variable, `-=`. For example, if you want to decrement the variable `a` by `2` instead of `1`, replace `a--` with `a-=2`.

{Try it}(sh .guides/bg.sh g++ code/operators/subtraction.cpp -o code/operators/subtraction ./code/operators/subtraction 3)



## Subtraction and Strings
You might be able to concatenate strings with the `+` operator, but you cannot use the `-` operator with them.

```c++
string a = "one two three";
string b = "one";
string c = a - b;
cout << c << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/subtraction.cpp -o code/operators/subtraction ./code/operators/subtraction 4)

{Check It!|assessment}(fill-in-the-blanks-1772784890)
