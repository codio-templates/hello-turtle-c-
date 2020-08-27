---

## The Min Function

The `min` function is another built-in function that returns the minimum value of a list.

```python
my_list = [45, 12, 9, 1]
smallest = min(my_list)
print(smallest)
```

{try it}(python3 code/lists/list-min.py 1)

|||challenge
## What happens if you:
* Change the value of `my_list` to `[0, 1, 0.5, -0.2, -1]`?
* Change the value of `my_list` to `[]`?

|||

{try it}(python3 code/lists/list-min.py 2)

## The Min Function & Strings

Unlike `sum`, the `min` function can work with strings. Python does this by selecting the element that comes first alphabetically.

```python
my_list = ["apple", "boy", "cat", "aaron"]
smallest = min(my_list)
print(smallest)
```

{try it}(python3 code/lists/list-min.py 3)

|||challenge
## What happens if you:
* Change the value of `my_list` to `["apple", "boy", "123", "cat"]`?
* Change the value of `my_list` to `["apple", "boy", 123, "cat"]`?

|||

{try it}(python3 code/lists/list-min.py 4)
