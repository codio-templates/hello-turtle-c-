---

## Tutorial Lab 2: Strings

You can use the `+` and `*` operators with strings, even though the result is not based on math. Using the `+` operator with strings is called concatenation.

Use the text editor open in the left pane, and enter the following code:

```c++
string string1 = "hip ";
string string2 = string1 + string1;
string string3 = "hoo";
string string4 = "ray!";
string string5 = string3 + string4;
cout << string2 << endl;
cout << string5 << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/labstrings.cpp -o code/operators/labstrings ./code/operators/labstrings 1)


1) Assign the value `"hip "` to the variable `string_1`. Note the inclusion of a space after the word `hip`.
2) The variable `string_2` will have the value `"hip hip "` because `string_1 + string_1` repeats the value of `string_1` two times.
3) Declare `string_3` and assign it the value `hoo`.
4) Declare `string_4` and assign it the value `ray!`.
5) Declare `string_5` and assign it the value of `string_3` combined with the value of `string_4` (`hooray!`).
6) Print the value of `string_2` (`hip hip `) without the newline character.
7) Print the value of `string_5` (`hooray!`) to the end of `string_2`.

{Check It!|assessment}(multiple-choice-1823701392)
