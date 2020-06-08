---

## Tutorial Lab 1: Arithmetic Operators

Arithmetic operations in Java are mostly the same as what you learned in math class. However, the symbols used in Java can be different.

|Operation|Symbol|Notes|
|---------|------|-----|
|Addition | + | |
|Subtraction | - | |
|Multiplication | * | |
|Division | / |Always returns a float|
|Modulo | % | Returns the remainder after division is performed|

Use the text editor open in the left pane, and enter the following code:

```c++
cout << 10 + 3 << endl;
cout << 10 - 3 << endl;
cout << 10 * 3 << endl;
cout << 10 / 3 << endl;
cout << 10 % 3 << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/labarithmetic.cpp -o code/operators/labarithmetic ./code/operators/labarithmetic 1)


1) Addition works as expected.
2) Subtraction works as expected.
3) Multiplication works as expected.
4) Division with integers will return a truncated integer result.
5) Modulo returns `1` because that is the remainder (not the decimal) after division is performed.

{Check It!|assessment}(fill-in-the-blanks-4285137417)
