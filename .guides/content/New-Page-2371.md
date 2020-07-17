---

## Printing without the Newline Character
The `cout` command does not add a newline character. The code below will print the two words on the same line without a space. Copy the code below into the text editor on the left and then click the `TRY IT` button below to see the output.

```c++
cout << "Hello";
cout << "world!";
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/tryit2.cpp -o code/fundamentals/tryit2 ./code/fundamentals/tryit2 1)

## Adding the Newline Character
The text in red shows the `endl` command which adds the newline character. (The newline character is what is inserted when you press "Enter" or "Return").


![.guides/img/NewlineCharacter](.guides/img/NewlineCharacter.png)

Add a second line by using the `cout << endl;` command under `"cout << "world!";`. Then enter the ouput command to print `My name is Codio.` Finally, click the `TRY IT` button to see the resulting output.

```c++
cout << "Hello";
cout << "world!";
cout << endl;
cout << "My name is Codio." << endl;
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/tryit2.cpp -o code/fundamentals/tryit2 ./code/fundamentals/tryit2 2)

|||challenge
## What happens if you:
* Add a `space` after `Hello` and before the closing `"`
* Add `<< endl;` after `cout << "Hello ";`
* Delete `cout << endl;` under `cout << "world!";`

|||

{Try it}(sh .guides/bg.sh g++ code/fundamentals/tryit2.cpp -o code/fundamentals/tryit2 ./code/fundamentals/tryit2 3)

{Check It!|assessment}(multiple-choice-4156149016)
