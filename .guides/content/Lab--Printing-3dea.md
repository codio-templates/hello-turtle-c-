---

## Tutorial Lab 1: Printing

1) In the text editor to your left, you will see the code below:

```c++
string my_var = "I am learning"; //step 1
cout << my_var; //step 2
my_var = " to program"; //step 3
cout << my_var; //step 4
my_var = " in C++."; //step 5
cout << my_var << endl; //step 6
my_var = "Hooray!"; //step 7
cout << my_var; //step 8
```

2) Click `TRY IT` to see what the code outputs.

{Try it}(sh .guides/bg.sh g++ code/fundamentals/labprinting.cpp -o code/fundamentals/labprinting ./code/fundamentals/labprinting 1)

3) Click on the ++underlined++ text below to highlight some of the important points in the code:
    * [Step 1](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 1" count=1) - Declare the variable `my_var` and initialize it to the value `I am learning`
    * [Step 2](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 2" count=1) - Print without a new line character by not including `<< endl;`
    * [Step 3](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 3" count=1) - Add a space when starting the string to avoid printing `learningto`
    * [Step 6](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 6" count=1) - A newline character is added using `<< endl;`
    * [Step 8](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 8" count=1) - `Hooray!` is on its own line since the `<< endl;` command was used in step 6

4) To remove the highlighting, click here: [Remove Highlighting](open_file code/fundamentals/labprinting.cpp panel=0)