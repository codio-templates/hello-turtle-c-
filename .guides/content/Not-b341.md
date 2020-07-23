---

## The `!` Operator

The `!` (not) operator produces the *opposite* result of the boolean expression that it modifies. 

```c++
cout << boolalpha << (! true) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/not.cpp -o code/operators/not ./code/operators/not 1)

|||challenge
## What happens if you:
* Replace `(! true)` in the code above with `(! true && false)`?
* Replace `(! true)` in the code above with `(! (true && false))`?
* Replace `(! true)` in the code above with `(! ! true)`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/not.cpp -o code/operators/not ./code/operators/not 2)

<details><summary>**Hint(s)**</summary>The `!` operator works similarly to how a `-` (negative) sign works in mathematics. The `-` of a positive number is a negative number and the `-` of a negative number is a positive number.</details>

## Order of Boolean Operators
Much like how arithmetic operators are evaluated in a certain order, boolean operators also work according to their priority level. Boolean operations are evaluated in the following order from highest to lowest priority:

1. Parentheses `()` 
2. Not `!`
3. And `&&`
4. Or `||`

{Check It!|assessment}(fill-in-the-blanks-111067014)
