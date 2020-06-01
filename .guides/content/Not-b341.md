---

## The `!` Operator

The `!` operator produces the opposite of the boolean expression that it modifies. 

```c++
System.out.println(! true);
```

{Try it}(sh .guides/bg.sh javac code/operators/PlaygroundNot.java java -cp code/operators/ PlaygroundNot 1)

|||challenge
## What happens if you:
* Change the code to `System.out.println(! true && false);`?
* Change the code to `System.out.println(! (true && false));`?
* Change the code to `System.out.println(! ! true);`?

|||

{Try it}(sh .guides/bg.sh javac code/operators/PlaygroundNot.java java -cp code/operators/ PlaygroundNot  2)

{Check It!|assessment}(fill-in-the-blanks-3532271981)

