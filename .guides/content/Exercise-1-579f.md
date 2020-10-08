---

## Conditionals Exercise 1

**Problem**
Use the variable `x` as you write this program. `x` will represent a positive integer. Write a program that determines if `x` is between 0 and 25 or between 75 and 100. If yes, print the message:`_ is between 0 and 25 or 75 and 100`, where the blank (`_`) will be the value of `x`. The program should do nothing if the value of `x` does not fit into either ranges.

**==Note:==** These are *inclusive* ranges - meaning if `x` is 0, 25, 75, or 100, the program should print out the message.

<details><summary><b>Type Casting</b></summary>Use the <code>to_string(x)</code> function to type cast the variable <code>x</code> as a string.</details><br>

**Expected Output**
* If `x` is `8`, then the output should be: `8 is between 0 and 25 or 75 and 100`.
* If `x` is `80`, then the output should be: `80 is between 0 and 25 or 75 and 100`.
* If `x` is `100`, then the output should be: `100 is between 0 and 25 or 75 and 100`.


### Click to compile your code

{Compile Code}(g++ code/conditionals/exercise1.cpp -o code/conditionals/exercise1)

### Test your code with a few different values

{Test with 8}(sh .guides/conditionals/exercise1.sh 8)

{Test with 80}(sh .guides/conditionals/exercise1.sh 80)

**==Note:==** This should output nothing. You should see Codio's default output of `Command was successfully executed.`
{Test with 50}(sh .guides/conditionals/exercise1.sh 50)

{Check It!|assessment}(code-output-compare-988115114)
