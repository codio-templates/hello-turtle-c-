---

## Integers
Integers (often called `int`s) are whole numbers. They can be positive or negative. Do not use a comma when typing large numbers.
  
Enter the code below and click the `TRY IT` button.
  
```c++
int number;
number = 50;
cout << number << endl;
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/integer.cpp -o code/fundamentals/integer ./code/fundamentals/integer 1)

Next, let's modify the code to look like what's below and click the `TRY IT` button again.

```c++
int number = 50;
cout << number << endl;
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/integer.cpp -o code/fundamentals/integer ./code/fundamentals/integer 2)

You may have noticed that we can declare a variable name and assign it a value all in one step by using `int number = 50;` instead of `int number;` followed by `number = 50;`. Both ways will produce the same result.

<details><summary><b>5 vs. "5"</b></summary>`5` is not the same thing as `"5"`. The first one is an integer, the second is a string. You will see in a later lesson the different operations you can perform on strings and numbers. Treating a string as a number can cause errors.</details>
  
|||challenge
## What happens if you:
* Change the variable to `5000`?
* Change the variable to `5,000`?
* Change the variable to `050`?
* Change the variable to `"5000"` (with double quotes)?

|||

{Try it}(sh .guides/bg.sh g++ code/fundamentals/integer.cpp -o code/fundamentals/integer ./code/fundamentals/integer 3)

{Check It!|assessment}(multiple-choice-2851726778)
