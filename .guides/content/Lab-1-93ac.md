---

## Odd or Even

Here is how you can iterate through a list, determine if the number is odd or even, and then put that number in a list of odd or even numbers. After the program has run, all of the odd numbers will be in the `odd` list and all of the even numbers will be in the `even` list.

### Random Numbers
To make this project more interesting, we are going to use a list of randomly generated ints. First, import the `random` library into your program.

```python
import random
```

Next, we are going to create a list called `numbers` and fill it with twenty random ints. Start my declaring the list `numbers` and make it an empty list (it has no elements). Then write a for loop that runs twenty times. Each time the loop runs, generate a random number and add it to the list.

```python
numbers = []
for i in range(20):
    numbers.append(random.randint(0, 100))
```

<details><summary>**The Random Library**</summary>To use the `random` library, you first import it with `import random`. To access any of the features of the library, start with `random.` and then add the method. Since we want a random integer, we will use `random.randint`. `randint` takes two numbers as parameters, the start and stop for the random number choice. We want a random integer between 0 and 100, so we use `random.randint(0, 100)`.</details>

### Odd and Even Lists
We are going to sort all of the random numbers into either the `even` list or the `odd` list. Create these lists and make them empty.

```python
odd = []
even = []
```

### Iterating Over `numbers`
Now we are going to iterate over the `numbers` list and determine if the number is even or odd.

```python
for number in numbers:
    if number % 2 == 0:
      
    else:
      
```

### Sorting the Elements
Once you have determined if a number is odd or even, use the `append` method to place it in the appropriate list.


```python
for number in numbers:
    if number % 2 == 0:
      even.append(number)
    else:
      odd.append(number)
```

### Printing the Lists
Let's print the three lists to see if our program worked. Don't forget to add some context to the lists. And to check our work, add together the lengths of `odd` and `even` to make sure they total 20.

```python
print("The odd numbers: ", odd)
print("The even numbers: ", even)
print(len(odd) + len(even))
```

{try it}(python3 code/lists/lab-odd-even.py 1)

<details><summary>**Code**</summary><img src=".guides/images/odd-even-list.png"></img></details>
