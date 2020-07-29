---

## For Loop Syntax
Before you can start writing a **loop**, you need to be able to spot the pattern. Let's take something simple:

```c++
cout << "Hello" << endl;
cout << "Hello" << endl;
cout << "Hello" << endl;
cout << "Hello" << endl;
cout << "Hello" << endl;
```

The pattern is `cout << "Hello" << endl;`, and it is repeated five times. Since we know that the loop needs to run exactly *five* times, a `for` loop can be used. Here is how you write a `for` loop that repeats five times. Copy the code below into the text editor on the left and then click on the `TRY IT` button to see the output. You can also click on the ++Code Visualizer++ link below to see how a `for` loop works behind the scenes. If the visualizer does not boot up correctly, click on the `Refresh code` button to restart it. Use the `Forward >` and `Back <` buttons to navigate the program.

```c++
for (int i = 0; i < 5; i++) {
  cout << "Hello" << endl;
}
```

{Try it}(sh .guides/bg.sh g++ code/loops/forloop.cpp -o code/loops/forloop ./code/loops/forloop 1)

[Code Visualizer](open_tutor code/loops/forloop.cpp)

Like **conditionals**, `for` loops are code blocks. However, in addition to a **boolean** statement(s), you also declare, initialize, and increment a **variable** called the loop **iterator**. All of the code that will be repeated are placed between the curly braces `{}`. It is *recommended* that you **indent** the code within the curly braces, but it is not necessary for the loop to run.

## Understanding the Loop Header
Copy the code below and `TRY IT`.

```c++
for (int i = 0; i < 5; i++) {
  cout << "Loop #" << i << endl;
}
```

{Try it}(sh .guides/bg.sh g++ code/loops/forloop.cpp -o code/loops/forloop ./code/loops/forloop 2)

[Code Visualizer](open_tutor code/loops/forloop.cpp)

The loop ran five times, but the variable `i` did not start at `1`. Instead, it started at `0`. C++ , like most programming languages, starts counting from 0 by default. C++ will continue counting up to, but not including, 5. The `i++` tells the system to continue counting up by `1` and the `i < 5` tells the system to stop counting *before* reaching 5.

|||challenge
## What happens if you:
* Replace `"Loop #" << i` in the code above to `"Loop #" << i + 1`?
* Replace `i < 5` with `i < 6` in the loop header and change the print statement back to `"Loop #" << i`?
* Replace `i < 5` with `i <= 5` in the loop header?
* Replace `i++` with `i--` in the loop header?

|||

{Try it}(sh .guides/bg.sh g++ code/loops/forloop.cpp -o code/loops/forloop ./code/loops/forloop 2)

[Code Visualizer](open_tutor code/loops/forloop.cpp)

<details><summary>**Infinite Loops**</summary>If you aren't careful, you can wind up with an **infinite loop**. This means that you have a loop that never ends. In the example above, if you change `i++` to `i--` then `i` will decrease by 1 after every iteration. This causes the loop iterator to never reach its specified value. The boolean expression continues to be true and the system continues to print until it times out. Always check your loop header to ensure that it does what you intend for it to do.</details>

{Check It!|assessment}(multiple-choice-4140309825)
