---

## The `||` Operator

The `||` (or) operator allows for compound (more than one) boolean expressions. If at least **one** boolean expression is true, then the whole thing is true. To be false, **all** boolean expressions **must** be false.

```c++
bool a = true;
bool b = true;
bool c = false;
bool d = false;
cout << boolalpha << (a || b) << endl;
```

<details><summary><b>How do I type <code>||</code>?</b></summary> It is towards the right-hand side, below the <code>backspace</code> or <code>delete</code> key and above the <code>enter</code> or <code>return</code> key. The <code>|</code> symbol is located on the same key as the <code>\</code> symbol. Hold <code>shift</code> and press the <code>\</code> key to type <code>|</code>. </details>

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 1)

|||challenge
## What happens if you:
* Replace `(a || b)` in the code above with `(a || c)`?
* Replace `(a || b)` in the code above with `(c || d)`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 2)

## Multiple `||` Statements

You can chain several `||` expressions together. They are evaluated in a left-to-right manner.

```c++
bool a = true;
bool b = true;
bool c = false;
cout << boolalpha << (a || b || c) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 3)

|||challenge
## What happens if you:
* Replace `(a || b || c)` in the code above with `(a || c || c || c || c)`?
* Replace `(a || b || c)` in the code above with `(c && c && c && c && c)`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 4)

{Check It!|assessment}(fill-in-the-blanks-1097451796)
