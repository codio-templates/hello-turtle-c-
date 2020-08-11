---

## Tutorial Lab 3: Breaking from the while loop
Use the text editor open in the left pane, and enter the following code:

<details><summary>What does `cin >> input;` mean?</summary>The `input` command will wait for the user to type some information into the terminal and press `return`. `input` takes an string argument which will be displayed for the user. The information entered by the user is stored in the variable `inp`. All information entered for the `input` command will be stored as a string (even if you type a number).</details>

```c++
int result = 0;

while (true) {
  cout << "Enter numbers to sum, enter q to quit" << endl;
  cin >> input;
  if (input != "q") {
    input = int(input)
    result = result + input;
  }
  else {
    cout << result << endl;
    break;
  }
}
```

{Try it}(sh .guides/bg.sh g++ code/loops/labbreak.cpp -o code/loops/labbreak ./code/loops/labbreak 1)

[Code Visualizer](open_tutor code/loops/labbreak.cpp)

1) Create the variable `result` and set its value to `0`. `result` will hold the total of the summation.
2) Next we set up a while loop with `True`. We do this because we want the loop to run until the user enters `q`. We don't know how long this will take, so we can limit the loop to a certain number of iterations.
3) We prompt the user to enter a number and use the built-in Python function `input`. `'> '` will appear, indicating that the user is to enter a value on the keyboard.
4) Next we assign the value the user enters to the `inp` variable.
5) Check to see if the value the user entered is `q`, for quit
6) If not, we convert the value to an integer with the `int()` command. This is required because the `input()` function returns a string value (you cannot add a string and an integer).
7) The `result` variable is updated to contain its current value plus the value entered by the user.
8) The loop continues accepting values and summing until the user enters the letter `q`. At that point, we step into the `else:` clause. We print the value of `result`, and then exit the loop with the `break` command.

