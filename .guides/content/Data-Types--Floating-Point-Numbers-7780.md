---

## Floating Point Numbers
Floating point numbers (often called floats) are numbers with a decimal. They can be positive or negative. Copy the code below and `TRY IT`.

```c++
double decimal = 0.5;
cout << decimal << endl;
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/double.cpp -o code/fundamentals/double ./code/fundamentals/double 1)

## Why Use Double Instead of Float?
In C++, there is a data type called **float**, but as it only uses 4 bytes, it is insufficient for most math. Instead, we use **double** which uses 8 bytes or double the space of a float.
  
|||challenge
## What happens if you:
* Change the variable to `50.`?
* Change the variable to `.001`?

|||

{Try it}(sh .guides/bg.sh g++ code/fundamentals/double.cpp -o code/fundamentals/double ./code/fundamentals/double 2)

{Check It!|assessment}(fill-in-the-blanks-3109256444)
