---

Your friend wrote a program called an **adder**. The adder is supposed to take two numbers inputted by a user and then find the sum of those numbers, but it's behaving oddly.

You can test the adder by using the terminal in the bottom-left panel. Once you click the `TRY IT` button below, the program will ask you to input two whole numbers. You need to press "Enter" or "Return" after typing each number.

{Try it | terminal}(g++ code/operators/exercise5.cpp -o code/operators/exercise5 && ./code/operators/exercise5 1 )

Your first task is to figure out what is wrong with the adder. Your second task is to fix it.

<details><summary>**Hint(s) to identify the problem**</summary>Try entering `1` and `1`. You expect the output to be `2` but you get `11` instead. Similarly, if you enter `3` and `4`, you expect the output to be `7` but you get `34`. Remember, **string concatenation** also uses the `+` operator.</details>

<details><summary>**Hint(s) to identify the solution**</summary>The `+` operator functions differently based on the type of data that comes before and after it. What data types will cause the `+` operator to calculate a **mathematical** sum? What data type is present in the program now? How do you convert from one data type to another? Check out the **Type Casting** page for some ideas. </details>

{Check It!|assessment}(code-output-compare-3680746899)
