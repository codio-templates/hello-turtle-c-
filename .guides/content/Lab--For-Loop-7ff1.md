---

## Tutorial Lab 1: Using the for loop
Copy the code below into the text editor on the left. Then click on the `TRY IT` button to see the resulting output and ++Code Visualizer++ link (below) to see how the program runs line by line.

```c++
for (int x = 0; x < 11; x++) {
  if (x % 2 == 0) {
    cout << "Even" << endl;
  }
  else {
    cout << "Odd" << endl;
  }
}
```

{Try it}(sh .guides/bg.sh g++ code/loops/labforloop.cpp -o code/loops/labforloop ./code/loops/labforloop 1)

[Code Visualizer](open_tutor code/loops/labforloop.cpp)

### Program Summary
1) The `for` loop runs through all the values of the variable `x` from 0 to 10 as specified in the loop header.
2) For each value of `x`, an expression is evaluated using a conditional `if` statement.
3) If `x` modulo `2` evaluates to 0, then print `Even` followed by a newline character.
4) If `x` modulo `2` *does not* evaluate to 0, then print `Odd` instead followed by a newline character.

{Check It!|assessment}(parsons-puzzle-3396681427)
