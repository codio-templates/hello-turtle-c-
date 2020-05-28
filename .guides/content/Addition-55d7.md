---

## Printing without the Newline Character
The `cout` command does not add a newline character. The code below will print the two words on the same line without a space. Click the `TRY IT` button below to see the output.

```c++
cout << "Hello";
cout << "world!";
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/tryit2.cpp -o code/fundamentals/tryit2 ./code/fundamentals/tryit2 1)

## The Addition (+) Operator
The addition operator works as you would expect with numbers.

```java
System.out.print(7 + 3);
```

{Try it}(sh .guides/bg.sh javac code/operators/PlaygroundAddition.java java -cp code/operators/ PlaygroundAddition 1 )

You can also add two variables together.

```java
int a = 7;
int b = 3;
System.out.print(a + b);
```

{Try it}(sh .guides/bg.sh javac code/operators/PlaygroundAddition.java java -cp code/operators/ PlaygroundAddition 2 )

|||challenge
## What happens if you:
* Make `a` of type double(e.g. `double a = 7.0;`)?
* Make `b` a negative number (e.g. `int b = -3;`)?
* Make `b` an explicitly positive number (e.g. `int b = +3;`)

|||

{Try it}(sh .guides/bg.sh javac code/operators/PlaygroundAddition.java java -cp code/operators/ PlaygroundAddition 3 )

{Check It!|assessment}(multiple-choice-225606126)
