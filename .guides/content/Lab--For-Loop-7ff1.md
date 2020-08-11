---

## Tutorial Lab 1: Using the for loop
Use the text editor open in the left pane, and enter the following code:

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

1) The for loop runs through all the values from 0 to 10, specified in the range command.
2) Then a comparison is made using an if statement.
3) If `x` modulo 2 results in 0, then print `Even`.
4) If `x` modulo 2 is any other number that is not 0, then print `Odd`.

