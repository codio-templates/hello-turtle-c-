---

## cout
The `cout` command is considered to be *non-specific* because you can use the same syntax for all of your printing needs (e.g. `cout << 1;`, `cout << "Hello";`, and `cout << true;`). However, for printing certain numbers, it is not always clear if what's printed is an `int` or a `double` sometimes.

```c++
int a = 1;
double b = 1.0;
cout << a << endl;
cout << b <<endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/printf.cpp -o code/operators/printf ./code/operators/printf 1)

Even though you are printing a `double` of `1.0`, the system will disregard the decimal and the trailing zero when `cout` is used. There is another print command called `printf()` that also prints text to the console.

## printf()
`printf()` originates from the C language and, unlike the `cout` command, it is considered to be *specific*. This means that you must specify what *type of data* you want to print before you can use the command successfully. 

```c++
int a = 1;
double b = 1.0;
cout << a << endl;
cout << b << endl;
printf("%d \n", a);
printf("%f \n", b);
```

{Try it}(sh .guides/bg.sh g++ code/operators/printf.cpp -o code/operators/printf ./code/operators/printf 2)

|||challenge
## What happens if you:
* Remove the `\n` from `printf("%d \n", a);`?
* Replace `%d` with `%f` in `printf("%d \n", a);`?
* Replace `%f` with `%d` in `printf("%f \n", b);`?

|||

|||important
## IMPORTANT
When `printf()` is used, a *specifier* is needed in order to tell the system what type of data you want to print. The `%d` tells the system to print an integer and `%f` tells the system to print a floating point number. If you use an incorrect specifier, you will receive an error message. By default, floating point numbers contain six zeros after the decimal point if they are printed using `printf()`.

The `\n` in `printf()` is equivalent to `endl`. They both print a newline character. Removing the `\n` from `printf("%d \n", a);` will delete the newline character and cause the variables `a` and `b` to be printed side-by-side.
|||

## cout vs. printf()
Unless you want to be *specific* with how your data is printed, you should always default to using `cout`. Only use `printf()` when formatting is important.

{Check It!|assessment}(multiple-choice-2926449521)
