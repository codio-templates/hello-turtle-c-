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

<details><summary><b>Hint(s)</b></summary><code>*=</code> works similarly to <code>+=</code>, <code>-=</code>, and <code>/=</code>.</details>

{Check It!|assessment}(multiple-choice-2185092284)
