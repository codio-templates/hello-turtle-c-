---

## Conditionals Exercise 3

**Problem**
Use the variable `x` as you write this program. `x` will represent a positive integer. Write a program that determines if `x` is divisible by 5 *and* is an even number. If yes, print `_ is divisible by 5 and even`, where the blank (`_`) is the value of `x`. If no, print `_ is not divisible by 5 or it is odd`, where the blank (`_`) is the value of `x`.

<details><summary><b>Type Casting</b></summary>Use the <code>to_string(x)</code> function to type cast the variable <code>x</code> as a string.</details><br>

**Expected Output**
* If `x` is `8`, then the output should be: `8 is not divisible by 5 or it is odd`.
* If `x` is `80`, then the output should be: `80 is divisible by 5 and even`.
* If `x` is `105`, then the output should be: `105 is not divisible by 5 or it is odd`.


### Click to compile your code

{Compile Code}(g++ code/conditionals/exercise3.cpp -o code/conditionals/exercise3)

### Test your code with a few different values

{Test with 8}(sh .guides/conditionals/exercise3.sh 8)

{Test with 80}(sh .guides/conditionals/exercise3.sh 80)

{Test with 105}(sh .guides/conditionals/exercise3.sh 105)

{Check It!|assessment}(code-output-compare-4008295054)
