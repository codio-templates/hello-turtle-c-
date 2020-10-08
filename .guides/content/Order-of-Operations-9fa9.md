---

## Order of Operations
C++ uses the **PEMDAS** method for determining order of operations.

![.guides/img/PEMDAS](.guides/img/PEMDAS.png)

By default, there are no operators for **exponents** and **square roots**. Instead, functions such `pow( , )` and `sqrt()` are used to calculate powers and square roots respectively. In order to use these functions, they must be imported by including `#include <cmath>` at top of the program header. For exponents, the *base* number goes before the `,` in `pow( , )` and the *exponent* goes after the `,`. For example, `pow(4, 2)` calculates $4^2$ and `pow(4, 0.5)` calculates $4^{0.5}$ or $4^{1/2}$. For square roots, the number goes inside the `()` in `sqrt()`. An example is `sqrt(4)` which calculates $\sqrt{4}$.

```c++
cout << pow(2, 2) << endl;
cout << pow(25, (1 / 2)) << endl;
cout << pow(25, (1.0 / 2.0)) << endl;
cout << sqrt(25) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/order.cpp -o code/operators/order ./code/operators/order 1)

<details><summary><b>pow(25, (1 / 2)) vs. pow(25, (1.0 / 2.0))</b></summary><code>pow(25, (1 / 2))</code> results in <code>1</code> because integer division is performed within <code>(1 / 2)</code>. <code>1</code> divided by <code>2</code> returns in an integer of <code>0</code> and $25^0$ computes to <code>1</code>. On the other hand, <code>pow(25, (1.0 / 2.0))</code> involves double division which is why <code>5</code> was computed.</details>

The code below should output `10.000000 `.

```c++
int a = 2;
int b = 3;
int c = 4;
double result = 3 * a - 2 / (b + 5) + c;
printf("%f \n", result);
```

{Try it}(sh .guides/bg.sh g++ code/operators/order.cpp -o code/operators/order ./code/operators/order 2)

<details><summary><b>Explanation</b></summary><ul><li>The first step is to compute <code>b + 5</code> (which is <code>8</code>) because it is surrounded by parentheses.</li><li>Next, do the multiplication and division going from left to right: <code>3 * a</code> is <code>6</code>.</li><li><code>2</code> divided by <code>8</code> is <code>0</code> (remember, the <code>/</code> operator returns an <code>int</code> when you use two <code>int</code>s so <code>0.25</code> becomes <code>0</code>).</li><li>Next, perform addition and subtraction from left to right: <code>6 - 0</code> is <code>6</code>.</li><li>Finally, add <code>6</code> and <code>4</code> together to get <code>10</code>.</li><li>Since <code>result</code> is of type <code>double</code>, <code>10.000000</code> is printed.</li></ul></details>

|||challenge
## Mental Math
<code>5 + 7 - 10 * 4 / 2</code><details><summary>Solution</summary>-8</details>
<code>5 * 8 - 7 % 2 - 18 * -1</code><details><summary>Solution</summary>57</details>
<code>9 / 3 + (100 % 100) - 3</code><details><summary>Solution</summary>0</details>
<code>12 - 2 * pow(2, 3) / (4 + 4)</code><details><summary>Solution</summary>10</details>

|||

{Try it}(sh .guides/bg.sh g++ code/operators/order.cpp -o code/operators/order ./code/operators/order 3)

{Check It!|assessment}(multiple-choice-2840268862)
