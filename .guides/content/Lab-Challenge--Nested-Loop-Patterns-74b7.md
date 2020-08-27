---

## Nested Loop Example
One of the benefits of nested loops is that they can be used to construct complex patterns. Imagine a classroom full of students and they are distributed evenly into smaller groups and asked to form a single line with their groups. The outer loop is like the group leader (represent in **red** and `L`) and the inner loop is like the rest of the group members (represented in **blue** and `M`.

<table>
<tr>

<td>
<div style="width:400px; height:550px; margin-left:120px">

![.guides/img/NestedLoopExample](.guides/img/NestedLoopExample.png)

</div>
</td>
</tr>
</table>

```c++
for (int x = 0; x < 3; x++) {
  cout << "L" << endl;
  for (int y = 0; y < 3; y++) {
    cout << "M" << endl;
  }
}
```

{Try it}(sh .guides/bg.sh g++ code/loops/labchallenge.cpp -o code/loops/labchallenge ./code/loops/labchallenge 1)

What is the pattern described by the above example? There are 3 leaders and **each** leader has 3 members. However, note that the example shows the students standing in a *vertical* line. What if you want to arrange the students in a *horizontal* line like this instead?

![.guides/img/NestedLoopHorizontal](.guides/img/NestedLoopHorizontal.png)

By removing the `<< endl` commands from the code above, you can accomplish this task. Alternatively, you can also make use of an `if` and `else` statement instead of a nested loop. Both ways will produce the same result.

<table>
<tr>
<td>
<div style="width:290px; height:180px">

```c++
for (int x = 0; x < 3; x++) {
  cout << "L";
  for (int y = 0; y < 3; y++) {
    cout << "M" <<;
  }
}
```

</div>
</td>
<td>
<div style="width:372px; height:180px">
          
```c++
for (int x = 0; x < 12; x++) {
  if ((x == 0) || (x == 4) || (x == 8)) {
    cout << "L";
  }
  else {
    cout << "M";
  }
}
cout << "" << endl;
```

</div>
</td>
</tr>
</table>

{Try it}(sh .guides/bg.sh g++ code/loops/labchallenge.cpp -o code/loops/labchallenge ./code/loops/labchallenge 1)

## Nested Loop Challenge
For this challenge, you will use your knowledge of **patterns**, **conditionals**, and **nested `for` loops** to produce the following output:
```c++
XOXOXOXOX
OXO
OXO
XOXOXOXOX
OXO
OXO
XOXOXOXOX
OXO
OXO
```

Your program **must** include **two** `for` loops, one nested within another, in order to receive credit.

{Try it}(sh .guides/bg.sh g++ code/loops/labchallenge.cpp -o code/loops/labchallenge ./code/loops/labchallenge 9)

{Check It!|assessment}(test-1015024454)
