---

## Tutorial Lab 3: Order of Operations

C++ uses PEMDAS when determining the order of operations.

![.guides/img/PEMDAS](.guides/img/PEMDAS.png)

<details><summary><b>Modulo and PEMDAS</b></summary>Since modulo is based on division, modulo operations happen at the time of multiplication and division, going from left to right.</details>

Use the text editor on the left to enter the following code:

```c++
cout << (5 * 8 / 3 + (18 - 8) % 2 - 25) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/labPEMDAS.cpp -o code/operators/labPEMDAS ./code/operators/labPEMDAS 1)

Below are the steps that C++ takes when evaluating the code above.
1) `5 * 8 / 3 + (18 - 8) % 2 - 25`
1) `5 * 8 / 3 + 10 % 2 - 25`
1) `40 / 3 + 10 % 2 - 25`
1) `13 + 10 % 2 - 25`
1) `13 + 0 - 25`
1) `13 - 25`
1) `-12`

{Check It!|assessment}(parsons-puzzle-1773163281)
