## Tutorial Lab 1: Printing

1) Use the code editor to the left.

2) Enter the code below.

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

3) `TRY IT` to see the output. Click on the ++Code Visualizer++ link below to go through the program step by step.

{Try it}(sh .guides/bg.sh g++ code/fundamentals/labprinting.cpp -o code/fundamentals/labprinting ./code/fundamentals/labprinting 1)

[Code Visualizer](open_tutor code/fundamentals/labprinting.cpp)

4) Here are some important points about the program (click on the underlined text):
    * [Step 1](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 1" count=1) - Declare the variable `my_var` and initialize it to the value `I am learning`
    * [Step 2](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 2" count=1) - Print without a new line character by not including `<< endl;`
    * [Step 3](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 3" count=1) - Add a space when starting the string to avoid printing `learningto`
    * [Step 6](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 6" count=1) - A newline character is added using `<< endl;`
    * [Step 8](open_file code/fundamentals/labprinting.cpp panel=0 ref="//step 8" count=1) - `Hooray!` is on its own line since the `<< endl;` command was used in step 6
