---

## Tutorial Lab 2: The while loop
Use the text editor open in the left pane, and enter the following code:

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

1) This loop will run as long as `counter` is less than 10.
2) Each time the loop runs, the value of `counter` is printed to the screen.
3) The value of `counter` is also incremented by 1.
4) At the end, a statement is printed to the screen, indicating the while loop has ended.
5) Recall that the while loop must have an exit condition. By incrementing the `counter` variable, we ensure that the loop will eventually end. If you do not increment `counter` in this loop, you will create an endless loop because `counter` will never reach 10 or greater.

