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

<details><summary>**Hint(s)**</summary>It is possible to declare and assign `int b = false;` because `false` is just a value of `0`. Since `5` is not less than `0`, `false` is returned.</details>

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

<details><summary>**Hint(s)**</summary>`false` is less than `true` because `0` is less than `1`.</details>

{Check It!|assessment}(multiple-choice-3904948409)
