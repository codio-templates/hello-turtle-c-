---

## Multiplication
C++ uses the `*` operator for multiplication.

```c++
int a = 5;
int b = 10;
cout << a * b << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/multiplication.cpp -o code/operators/multiplication ./code/operators/multiplication 1)

|||challenge
## What happens if you:
* Assign `b` to `0.1`?
* Assign `b` to `-3`?
* Change the code to...
```c++
int a = 5;
int b = 10;
a*=b;
cout << a << endl;
```
|||

{Try it}(sh .guides/bg.sh g++ code/operators/multiplication.cpp -o code/operators/multiplication ./code/operators/multiplication 2)

<details><summary>**Hint(s)**</summary>`*=` works similarly to `+=`, `-=`, and `/=`.</details>

{Check It!|assessment}(multiple-choice-2185092284)
