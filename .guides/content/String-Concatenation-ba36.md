---

## String Concatenation
String concatenation is the act of combining two strings together. This is done with the `+` operator.

```c++
string a = "This is an ";
string b = "example string";
string c = a + b;
cout << c << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/concatenation.cpp -o code/operators/concatenation ./code/operators/concatenation 1)

|||challenge
## What happens if you:
* Concatenate two strings without an extra space (e.g. remove the space after `an` in `string a = "This is an";`)?
* Use the `+=` operator instead of the `+` operator (e.g. `a+=b` instead of `a + b`)?
* Add `3` to a string (e.g. `string c = a + b + 3;`)?
* Add `"3"` to a string (e.g. `string c = a + b + "3";`)?

|||

{Try it}(sh .guides/bg.sh g++ code/operators/concatenation.cpp -o code/operators/concatenation ./code/operators/concatenation 2)

{Check It!|assessment}(parsons-puzzle-2622494909)
