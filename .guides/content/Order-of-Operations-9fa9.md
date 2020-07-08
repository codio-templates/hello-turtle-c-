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

<details><summary>**pow(25, (1 / 2)) vs. pow(25, (1.0 / 2.0))**</summary>`pow(25, (1 / 2))` results in `1` because integer division is performed within `(1 / 2)`. `1` divided by `2` returns in an integer of `0` and $25^0$ computes to `1`. On the other hand, `pow(25, (1.0 / 2.0))` involves double division which is why `5` was computed.</details>

The code below should output `10.000000 `.

```c++
int a = 2;
int b = 3;
int c = 4;
double result = 3 * a - 2 / (b + 5) + c;
printf("%f \n", result);
```

{Try it}(sh .guides/bg.sh g++ code/operators/order.cpp -o code/operators/order ./code/operators/order 2)

<details><summary>**Explanation**</summary><ul><li>The first step is to compute `b + 5` (which is `8`) because it is surrounded by parentheses.</li><li>Next, do the multiplication and division going from left to right: `3 * a` is `6`.</li><li>`2` divided by `8` is `0` (remember, the `/` operator returns an `int` when you use two `int`s so `0.25` becomes `0`).</li><li>Next, perform addition and subtraction from left to right: `6 - 0` is `6`.</li><li>Finally, add `6` and `4` together to get `10`.</li><li>Since `result` is of type `double`, `10.000000` is printed.</li></ul></details>

|||challenge
## Mental Math
* `5 + 7 - 10 * 4 / 2`
<details><summary>Solution</summary>-8</details>
* `5 * 8 - 7 % 2 - 18 * -1`
<details><summary>Solution</summary>57</details>
* `9 / 3 + (100 % 100) - 3`
<details><summary>Solution</summary>0</details>
* `12 - 2 * pow(2, 3) / (4 + 4)`
<details><summary>Solution</summary>10</details>

|||

{Try it}(sh .guides/bg.sh g++ code/operators/order.cpp -o code/operators/order ./code/operators/order 3)

{Check It!|assessment}(multiple-choice-2840268862)
