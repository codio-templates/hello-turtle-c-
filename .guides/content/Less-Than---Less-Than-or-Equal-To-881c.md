---

## Less Than

The `<` operator is used to check if one value is less than another value.

```c++
int a = 5;
int b = 7;
cout << boolalpha << (a < b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 1)

|||challenge
## What happens if you:
* Change `b` to `1`?
* Change `b` to `5`?
* Change `b` to `false`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 2)

## Less Than or Equal To

The `<=` operator is used to check if one value is less than or equal to another value.
```c++
int a = 5;
int b = 7;
cout << boolalpha << (a <= b) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 3)

|||challenge
## What happens if you:
* Change `b` to `1`?
* Change `b` to `5`?
* Change `a` to `false` and `b` to `true`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/lessthan.cpp -o code/operators/lessthan ./code/operators/lessthan 4)

{Check It!|assessment}(multiple-choice-3157845998)
