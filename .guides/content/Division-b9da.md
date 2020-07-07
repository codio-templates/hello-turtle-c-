---

## Division

Division in C++ is done with the `/` operator.

```c++
double a = 25;
double b = 4;
printf("%f \n", a / b);
```

{Try it}(sh .guides/bg.sh g++ code/operators/division.cpp -o code/operators/division ./code/operators/division 1)

|||challenge
## What happens if you:
* Assign `b` to `0`?
* Assign `b` to `0.5`?
* Change the code to look like what's below
```c++
double a = 25;
double b = 4;
a /= b;
printf("%f \n", a);
```

|||

{Try it}(sh .guides/bg.sh g++ code/operators/division.cpp -o code/operators/division ./code/operators/division 2)

|||important
## IMPORTANT
Division by zero is *undefined* in mathematics. In C++, dividing by zero results in *infinity* and thus `inf` was returned when you tried to divide by `0`. 
|||

<details><summary>**Hint**</summary>`/=` works similarly to `+=` and `-=`.</details>

## Integer Division

Normally, you use `double` in C++ division since the result usually involves decimals. If you use integers, the division operator returns an `int`. This "integer division" does not round up, nor round down. It removes the decimal value from the answer.

![.guides/img/IntDivision](.guides/img/IntDivision.png)

```c++
int a = 5;
int b = 2;
cout << a / b << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/division.cpp -o code/operators/division ./code/operators/division 3)

{Check It!|assessment}(multiple-choice-3824135241)
