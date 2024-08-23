# For Loop

The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or any other iterable object. It allows you to execute a block of code a specific number of times, usually determined by the length of the sequence or the range of values.

### Syntax

```
for item in iterable:
    # Execute this block of code
```

### Iterating over a list

```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Iterating over a string

```
for letter in "Python":
    print(letter)
```

### Using range() in a for loop

```
for i in range(5):
    print(i)
```

### Specifying a start and end in range()

```
for i in range(2, 6):
    print(i)
```

### Using a step in range()

```
for i in range(1, 10, 2):
    print(i)
```

### for Loop with zip()
Iterating over two lists simultaneously

```
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

---

# Nested for Loops

Nested for loops are used when you need to perform an action that involves iterating over multiple sequences or when dealing with multi-dimensional data (like a matrix or list of lists).


### Iterating over a list of lists

``` matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

