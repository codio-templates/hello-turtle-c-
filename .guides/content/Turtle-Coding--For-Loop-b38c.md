---
## Customize Your Turtle
You may choose to change the dimensions of your turtle screen whenever you'd like. Also, the following table provides additional commands you can use to customize `tina` the turtle.

|Command|Parameter|Examples|
|:-----:|:-------:|:---------:|
|`tina.pencolor({"COLOR"})`|Where `COLOR` represents the track or line color you want tina to leave behind|red, orange, yellow, green, blue, purple|
|`tina.width(W)`|Where `W` represents how wide (in pixels) tina's track is|any positive integer (e.g. 1, 10, 123, etc.)|
|`tina.shape("SHAPE")`|Where `SHAPE` represents the shape tina takes|triangle, indented triangle, square, arrow|
|`tina.speed(SPEED)`|Where `SPEED` represents how fast tina moves|TS_FASTEST, TS_FAST, TS_NORMAL, TS_SLOW, TS_SLOWEST|

## Turtle Challenges
Now that you know how to customize `tina`, try to recreate the images you see below using your knowledge of `for` loops.

### Challenge 1
![.guides/img/TurtleChallenge1](.guides/img/TurtleChallenge1.gif)
{Try it|terminal}(bash .guides/turtle.sh g++ turtlechallenge.cpp -o turtlechallenge ./turtlechallenge)

<details><summary><b>Hint</b></summary>There are multiple ways to accomplish this task but the trick lies within finding the <b>pattern</b> and then repeating it a <b>specific number of times</b>. One pattern in particular is to: <ol><li>Go forward (creating a long line).</li><li>Make a right turn.</li><li>Go forward (creating a small line).</li><li>Make a right turn.</li><li>Go forward (creating another small line).</li><li>Make a right turn.</li><li>Go forward (creating a final small line).</li><li>Repeat steps #1 through #7 three more times for a total of <b>four</b> iterations.</li></ol>The pattern should look something like this: <img src=".guides/img/TurtleChallenge1Pattern.png"/></details>

### Challenge 2
![.guides/img/TurtleChallenge2](.guides/img/TurtleChallenge2.gif)
{Try it|terminal}(bash .guides/turtle.sh g++ turtlechallenge.cpp -o turtlechallenge ./turtlechallenge)

<details><summary><b>Hint</b></summary>Since a circle has 360 degrees, you will need a loop that repeats 360 times. Be careful about how far the turtle moves forward and turns. The circle can get very big, very quickly.</details>

### Challenge 3
![.guides/img/TurtleChallenge3](.guides/img/TurtleChallenge3.gif)
{Try it|terminal}(bash .guides/turtle.sh g++ turtlechallenge.cpp -o turtlechallenge ./turtlechallenge)

<details><summary><b>Hint</b></summary>The pattern here is to move forward and make a right turn. <img src=".guides/img/TurtleChallenge3Pattern.png"/> 
The trick lies within the fact that the distance the turtle moves has to get larger as the loop advances. Think of some operators that you can use to make the loop iterator variable get bigger during each iteration.</details>

|||info
### NOTE
Due to the dynamic and graphical nature of the Turtle Graphics library, **jagged** lines and **spotty** pixels may appear randomly as the output is being drawn. This is completely **normal**!

![.guides/img/CppJaggedLine](.guides/img/CppJaggedLine.png)

|||

<table><tbody ><tr><td><details><summary>
	<b>Still having trouble with creating the outputs above?</b>
</summary><br>
Here are some sample solutions:
  
```c++
  tina.pencolor({"blue"});
  tina.width(2);
  tina.shape("arrow");
  tina.speed(TS_SLOWEST);
  
  for (int i = 0; i < 4; i++) {
    tina.forward(75);
    tina.right(90);
    tina.forward(25);
    tina.right(90);
    tina.forward(25);
    tina.right(90);
    tina.forward(25);
  }
```

```c++
  tina.pencolor({"red"});
  tina.width(2);
  tina.shape("square");
  tina.speed(TS_FASTEST);
  
  for (int i = 0; i < 360; i++) {
    tina.forward(1);
    tina.right(1);
  }
```
  
```c++
  tina.pencolor({"green"});
  tina.width(2);
  tina.shape("triangle");
  tina.speed(TS_NORMAL);
  
  for (int i = 10; i <= 200; i+=10) {
    tina.forward(i);
    tina.right(90);
  }
```

</details></td></tr></tbody>
</table>

{Check It!|assessment}(fill-in-the-blanks-709209464)
