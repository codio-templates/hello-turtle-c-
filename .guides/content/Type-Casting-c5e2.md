---

## Type Casting
Type casting (or type conversion) is when you change the data type of a variable.

```c++
int numerator = 40;
int denominator = 25;
cout << numerator / denominator << endl;
cout << (double) numerator / denominator << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/casting.cpp -o code/operators/casting ./code/operators/casting 1)

`numerator` and `denominator` are integers, but `(double)` converts `numerator` into a double.

|||challenge
## What happens if you:
* Cast only `denominator` to a double?
* Cast both `numertor` and `denominator` to a double?
* Cast the result to a double (i.e. `(double)(numerator / denominator)`)?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/casting.cpp -o code/operators/casting ./code/operators/casting 2)

<details><summary><b>More Info</b></summary>If either or both numbers in Java division are a `double`, then `double` division will occur. In the last example, numerator and denominator are both `int` when the division takes place - then the integer division result is converted to a double. </details>

## Parsing Strings
Do you know why the code below will not work?

```c++
int a = 5;
string b = "3";
cout << a + b << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/casting.cpp -o code/operators/casting ./code/operators/casting 3)

You cannot add a string to an integer. You can convert `b` to an integer to fix the problem.

```c++
int a = 5;
string b = "3";
cout << a + stoi(b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/casting.cpp -o code/operators/casting ./code/operators/casting 4)

Data read from the keyboard or a file is always stored as a string. If you want to use this data, you will need to know how to convert it to the proper data type.

|||challenge
## What happens if you:
* Parse a String to a double using `stod()`
* // Parse a String to a boolean using `boolalpha`
* // Convert a different type to a string with `String.valueOf()`

|||

{Check It!|assessment}(multiple-choice-2976548927)
