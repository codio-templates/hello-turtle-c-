---

## Cross-Referencing Colors
Write a program that cross-references a list of random colors with lists of warm, cool, and neutral colors. Keep track of how many warm, cool, and neutral colors are in the list of random colors. Also keep track of how many colors do not appear in any of the lists.

### Setup
The lists `warm`, `cool`, and `neutral` are already provided. We will need a list `colors` filled with a randomly selected colors. We will also need the variables `warm_count`, `cool_count`, `neutral_count`, and `misc_count` to keep track of how often these colors appear. These variables can be set to 0.

```python
colors = ["red", "black", "pink", "beige", "dark green", "azure", "amber", "light yellow"]
warm_count = 0
cool_count = 0
neutral_count = 0
misc_count = 0
```

### Iterating
There are a couple of ways to solve this problem. You could iterate over the `warm` list and see if any of the elements in `colors` are present. You would repeat this with the `cool` and `neutral` lists as well. The problem arises when you try and figure out what are miscellaneous colors. There is no list for this. A miscellaneous color would any color that is not in the `warm`, `cool`, or `neutral` lists. Instead, iterate over the `colors` list and see if each element is in the `warm`, `cool`, or `neutral` lists. If an element is not in those three lists, then it is a miscellaneous color.

```python
for color in colors:
    
```

### Conditionals
The order of conditionals is not important. Let's start with the `warm` list. If the element is in this list, increment the `warm_count` variable. Use `elifs` for the other lists, and increment the respective variable.

```python
for color in colors:
   if color in warm:
      warm_count += 1
   elif color in cool:
      cool_count += 1
   elif color in neutral:
      neutral_count += 1
```

### Miscellaneous Colors
If all of these conditionals are false, then the color can be considered miscellaneous. Use an `else` statement to increment the `misc_count` variable.

```python
for color in colors:
   if color in warm:
      warm_count += 1
   elif color in cool:
      cool_count += 1
   elif color in neutral:
      neutral_count += 1
   else:
      misc_count += 1
```

### Printing the Answer and Checking our Work
Let's start by printing the length of `colors` with a message. Then print the values of `warm_count`, `cool_count`, `neutral_count`, and `misc_count` with a respective message. The sum of these variables should equal the length of `colors`.

```python
print("The total # of colors is ", len(colors))
print("There are ", warm_count, " warm colors")
print("There are ", cool_count, " cool colors")
print("There are ", neutral_count, " neutral colors")
print("There are ", misc_count, " miscellaneous colors")
```

<details><summary>**What Happened to the `+` Operator?**</summary>You may have noticed that the string concatenation operator (`+`) is not used in the `print` statements. To use concatenation, you must have two strings. Which means you need to type cast the integer variables as strings. Python also lets you use a variable in a string by using a comma to separate the variable from the strings. No type casting is necessary. Both options do the same things.</details>

<details><summary>**Code**</summary><img src=".guides/images/sort-colors-code.png"/></details>

{try it}(python3 code/lists/lab-color-sort.py)
