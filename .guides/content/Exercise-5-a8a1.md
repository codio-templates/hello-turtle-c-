---

Your friend wrote a program called an **adder**. The adder is supposed to take two numbers inputted by a user and then find the sum of those numbers, but it's behaving oddly.

You can test the adder by using the terminal in the bottom-left panel. Once you click the `TRY IT` button below, the program will ask you to input two whole numbers. You need to press "Enter" or "Return" after typing each number.

{Try it | terminal}(g++ code/operators/exercise5.cpp -o code/operators/exercise5 && ./code/operators/exercise5 1 )

Your first task is to figure out what is wrong with the adder. Your second task is to fix it.

<details><summary><b>Hint(s) to identify the problem</b></summary>Try entering <code>1</code> and <code>1</code>. You expect the output to be <code>2</code> but you get <code>11</code> instead. Similarly, if you enter <code>3</code> and <code>4</code>, you expect the output to be <code>7</code> but you get <code>34</code>. Remember, <b>string concatenation</b> also uses the <code>+</code> operator.</details>

<details><summary><b>Hint(s) to identify the solution</b></summary>The <code>+</code> operator functions differently based on the type of data that comes before and after it. What data types will cause the <code>+</code> operator to calculate a <b>mathematical</b> sum? What data type is present in the program now? How do you convert from one data type to another? Check out the <b>Type Casting</b> page for some ideas. </details>

{Check It!|assessment}(code-output-compare-3680746899)
