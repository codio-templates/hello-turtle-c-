---

## Subtraction

```c++
int a = 10;
int b = 3;
int c = a - b;
cout << c << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/subtraction.cpp -o code/operators/subtraction ./code/operators/subtraction 1)

|||challenge
## What happens if you:
* Change `b` to `-3`?
* Change `c` to `c = a - -b`?
* Change `b` to `3.0`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/subtraction.cpp -o code/operators/subtraction ./code/operators/subtraction 2)

## The `--` and `-=` Operators
Decrementing is the opposite of incrementing. Just like you can increment with `++`, you can decrement using `--`.

```c++
int a = 10;
a--;
cout << a << endl;
```

Like `+=`, there is a shorthand for decrementing a variable - `-=`.

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

{Check It!|assessment}(fill-in-the-blanks-436876892)
