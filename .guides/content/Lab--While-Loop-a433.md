---

## Tutorial Lab 2: The While Loop
Copy the code below into the text editor on the left. Then click on the `TRY IT` button to see the resulting output and ++Code Visualizer++ link (below) to see how the program runs line by line.

```c++
int counter = 0;
while (counter < 10) {
  cout << counter << endl;
  counter = counter + 1;
}
cout << "while loop ended" << endl;
```

{Try it}(sh .guides/bg.sh g++ code/loops/labwhileloop.cpp -o code/loops/labwhileloop ./code/loops/labwhileloop 1)

[Code Visualizer](open_tutor code/loops/labwhileloop.cpp)

### Program Summary
1) A `counter` variable is initialized to keep track of how many times the loop will be executed.
2) The loop will run as long as `counter` is less than 10.
3) Each time the loop runs, the integer value of `counter` is printed to the screen.
4) The value of `counter` is then incremented by 1.
5) When `counter` reaches `10`, the boolean expression no longer evaluates to true and the program will exit the loop.
6) Before the program terminates, a statement is printed to the screen, indicating that the `while` loop has ended.
7) Recall that the `while` loop must have an exit condition. By incrementing the `counter` variable, we ensure that the loop will eventually end. If we do not increment `counter` in this loop, we will create an *infinite* loop because `counter` will never reach 10 or greater.

{Check It!|assessment}(multiple-choice-3422329539)
