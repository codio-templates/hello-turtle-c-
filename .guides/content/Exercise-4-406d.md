---

## Conditionals Exercise 4

**Problem**
Use the variable `x` as you write this program. `x` will represent a string. Write a program that determines if `x` is a primary color (red, blue, or yellow). If yes, print `_ is a primary color`, where the blank (`_`) is the value of `x`. If no, print `_ is not a primary color`, where the blank (`_`) is the value of `x`. For this particular exercise, make sure that your code *specifically* checks if the variable `x` is equivalent to the strings `red`, `blue`, or `yellow` in all **lowercase**. Otherwise, your test cases will fail.

|||important
## IMPORTANT
There is a difference between all of the following strings: "red", "Red", and "RED". When comparing strings, the system is **case-sensitive** and will attempt to match each character of the strings to each other based on whether it is uppercase or lowercase. 
|||

**Expected Output**
* If `x` is `red`, then the output would be: `red is a primary color`.
* If `x` is `teal`, then the output would be: `teal is not a primary color`.

### Click to compile your code

{Compile Code}(g++ code/conditionals/exercise4.cpp -o code/conditionals/exercise4)

### Test your code with a few different values

{Test with "red"}(sh .guides/conditionals/exercise4.sh red)

{Test with "teal"}(sh .guides/conditionals/exercise4.sh teal)

{Check It!|assessment}(code-output-compare-3027926170)
