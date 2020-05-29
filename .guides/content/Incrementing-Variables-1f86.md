---

## Incrementing Variables
Incrementing a variable means to increase the value of a variable by a set amount. The most common incrementation you will see is when a variable increments itself by the value of 1. Copy the code below and `TRY IT`.

```c++
int a = 0;
a = a + 1;
cout << a << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/increment.cpp -o code/operators/increment ./code/operators/increment 1)

## How to Read `a = a + 1`
The variable `a` appears twice on the same line of code. But each instance of `a` refers to something different.

![.guides/img/increment](.guides/img/increment.png)

## The `++` and `+=` Operators
Since incrementing is such a common task for programmers, many programming languages have developed a shorthand for `a = a + 1`. The result is `a++` which does the same thing as `a = a + 1`. `TRY IT` below.

```c++
int a = 0;
int b = 0;
a = a + 1;
b++;
cout << a << endl;
cout << b << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/increment.cpp -o code/operators/increment ./code/operators/increment 2)

In the cases where you need to increment by a different number, you can specify it by using the `+=` operator. You can replace `b++;` with `b+=1;` in the above code and still get the same result.

|||challenge
## What happens if you:
* Replace `b++` in the above code with `b+=2`?
* Replace `b++` in the above code with `b+=-1`?
* Replace `b++` in the above code with `b-=1`?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/increment.cpp -o code/operators/increment ./code/operators/increment 3)

{Check It!|assessment}(multiple-choice-1014071651)

