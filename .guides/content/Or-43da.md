---

## The `||` Operator

The `||` operator allows for compound (more than one) boolean expressions. If only one boolean expressions is true, then the whole thing is true. To be false, **all** boolean expressions must be false.

```c++
boolean a = true;
boolean b = true;
boolean c = false;
boolean d = false;
System.out.println(a || b);
```

<details><summary><b>How do I type `||`?</b></summary> It is on the right-hand side, below the backspace/delete key and above the enter/return key. The `|` symbol is the line above the `\`. This means you must hold shift and press the `\` key to type `|`. </details>

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 1)

|||challenge
## What happens if you:
* Change the code to `System.out.println(a || c);`?
* Change the code to `System.out.println(c || d);`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 2)

## Multiple `||` Statements

You can chain several `||` statements together. They are evaluated in a left-to-right manner.

```c++
boolean a = true;
boolean b = true;
boolean c = false;
System.out.println(a || b || c);
```

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 3)

|||challenge
## What happens if you:
* Change the code to 
`System.out.println(a || c || c || c || c);`?
* Change the code to 
`System.out.println(c && c && c && c && c);`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/or.cpp -o code/operators/or ./code/operators/or 4)

{Check It!|assessment}(fill-in-the-blanks-3858330751)
