---

## Printing to the Console
As you learn C++, you will write code in the text editor to the left. *There is already some code there that we will cover later*. For now, use a `cout` command to see the output of your program. Copy and paste the code below into the text editor on the left. Make sure your code is in between the `//add code below this line` and `//add code above this line` comments. Then click the `TRY IT` button to see what is outputted by the code.

```c++
cout << "Hello world!";
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/tryit1.cpp -o code/fundamentals/tryit1 ./code/fundamentals/tryit1 1)

The reason you were able to see the words appear is because of the `cout` command followed by the `<<` and finally what you want to print `"Hello world";`. __cout__ is short for *characters out* and is used to output your desired text.

Change your desired output to look like this and `TRY IT` again.

```c++
"My name is Codio."
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/tryit1.cpp -o code/fundamentals/tryit1 ./code/fundamentals/tryit1 2)

{Check It!|assessment}(multiple-choice-3602415844)
