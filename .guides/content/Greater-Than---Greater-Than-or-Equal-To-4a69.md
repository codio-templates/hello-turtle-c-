---

## Greater Than

The `>` operator is used to check if one value is *greater* than another value.

```c++
int a = 9;
int b = 17;
cout << boolalpha << (a > b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/greaterthan.cpp -o code/operators/greaterthan ./code/operators/greaterthan 1)

|||challenge
## What happens if you:
* Assign `b` to `1`?
* Assign `b` to `9`?
* Assign `b` to `false`?
* Assign `b` to `true`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/greaterthan.cpp -o code/operators/greaterthan ./code/operators/greaterthan 2)

<details><summary><b>Hint(s)</b></summary><code>9</code> is both greater than the value of <code>false</code>, which is <code>0</code>, and the value of <code>true</code>, which is <code>1</code>.</details>

## Greater Than or Equal To

The `>=` operator is used to check if one value is *greater than or equal* to another value.
```c++
int a = 9;
int b = 17;
cout << boolalpha << (a >= b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/greaterthan.cpp -o code/operators/greaterthan ./code/operators/greaterthan 3)

|||challenge
## What happens if you:
* Assign `b` to `1`?
* Assign `b` to `9`?
* Assign `a` to `true` and assign `b` to `false`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/greaterthan.cpp -o code/operators/greaterthan ./code/operators/greaterthan 4)

<details><summary><b>Hint(s)</b></summary><code>true</code> is greater than <code>false</code>.</details>

{Check It!|assessment}(multiple-choice-1809804957)
