---

## Short Circuiting

If Java can determine the result of a boolean expression before evaluating the entire thing, it will stop and return the value.

![Short Circuiting](.guides/img/shortcircuiting.png)

```c++
cout << boolalpha << ( false 
                             && 
/*C++ never reaches this line*/ true) << endl; 

cout << boolalpha << ( true 
                             || 
/*C++ never reaches this line*/ false) << endl;
```

{Try it}(sh .guides/bg.sh g++ code/operators/shortcircuiting.cpp -o code/operators/shortcircuiting ./code/operators/shortcircuiting 1)

{Check It!|assessment}(fill-in-the-blanks-1476766980)
