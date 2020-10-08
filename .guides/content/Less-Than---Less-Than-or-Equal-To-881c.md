---

## Less Than

The `<` operator is used to check if one value is *less than* another value.

```c++
int a = 5;
int b = 7;
cout << boolalpha << (a < b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 1)

|||challenge
## What happens if you:
* Assign `b` to `1`?
* Assign `b` to `5`?
* Assign `b` to `false`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 2)

<details><summary><b>Hint(s)</b></summary>It is possible to declare and assign <code>int b = false;</code> because <code>false</code> is just a value of <code>0</code>. Since <code>5</code> is not less than <code>0</code>, <code>false</code> is returned.</details>

## Less Than or Equal To

The `<=` operator is used to check if one value is *less than or equal to* another value.
```c++
int a = 5;
int b = 7;
cout << boolalpha << (a <= b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 3)

|||challenge
## What happens if you:
* Assign `b` to `1`?
* Assign `b` to `5`?
* Assign `a` to `false` and assign `b` to `true`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 4)

<details><summary><b>Hint(s)</b></summary><code>false</code> is less than <code>true</code> because <code>0</code> is less than <code>1</code>.</details>

{Check It!|assessment}(multiple-choice-3904948409)
