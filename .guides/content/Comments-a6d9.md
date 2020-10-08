---

## Comments
You may have wondered why a couple of lines of code are a different color (in the below example, light brown, but it depends on the Theme you have picked):

![.guides/img/Comment](.guides/img/Comment.png)

In C++, to write notes in code without affecting its function, we can use `//` to make a **single-line comment**. Click the `TRY IT` button below to see the resulting output.

{Try it}(sh .guides/bg.sh g++ code/fundamentals/comments.cpp -o code/fundamentals/comments ./code/fundamentals/comments 1)

Comments can also be used to help you fix your code. You can “comment out” lines of code that are not working or you suspect are causing problems.

|||challenge
## What happens if you:
* Change `cout << "Red"` to `cut << "Red"`
* Add `//` in front of `cut << "Red"`

|||

{Try it}(sh .guides/bg.sh g++ code/fundamentals/comments.cpp -o code/fundamentals/comments ./code/fundamentals/comments 2)

## Block Comments
To make a **block comment** you can either make multiple single-line comments using `//` or wrap the set of lines in `/*` and `*/`. `TRY IT` below!

```c++
/*
This is the start of a multi-line comment.
You can end the comment with a star(*) followed by a forward slash(/).
*/

//You can also do a multi-line comment
//like this!
    
cout << "Notice how the comments above are lightly faded.";
cout << "Most IDEs automatically lighten the comments.";
cout << "This is a common feature known as syntax highlighting.";
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/comments.cpp -o code/fundamentals/comments ./code/fundamentals/comments 3)

<details><summary><b>What is an IDE?</b></summary><i>An integrated development environment, or IDE, is a computer program that makes it easier to write other computer programs. They are used by computer programmers to edit source code, and can be easier to use than other text editors for new programmers. They can have compilers so programmers don’t have to open other programs to compile the source code. They also often have syntax highlighting. ... It also may have predictive coding that can finish lines with syntax such as brackets or semicolons and can suggest variables to be used. It also may have debuggers that can step through lines, take breaks and inspect variables.</i><br><b>Source: Simple Wikipedia</b></details>

{Check It!|assessment}(fill-in-the-blanks-1342485909)
