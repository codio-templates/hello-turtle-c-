---

## Modulo

Modulo is the mathematical operation that performs division but returns the remainder. The modulo operator is `%`.

![Modulo](.guides/img/modulo.png)

```c++
int modulo = 5 % 2;
cout << modulo << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/modulo.cpp -o code/operators/modulo ./code/operators/modulo 1)

|||challenge
## What happens if you:
* Change `modulo` to `5 % -2`?
* Change `modulo` to `5 % 0`?
* Change `modulo` to `5 % 2.0`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/modulo.cpp -o code/operators/modulo ./code/operators/modulo 2)

{Check It!|assessment}(multiple-choice-2865610959)
