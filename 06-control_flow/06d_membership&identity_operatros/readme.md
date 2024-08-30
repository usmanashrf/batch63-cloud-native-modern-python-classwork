# Membership & Identity Operators

Membership and identity operators in Python are used to check the presence of an element within a sequence and to compare objects' identities, respectively. Here's an explanation of each:

## Membership Operators

Membership operators are used to test whether a value or variable is found within a sequence, such as a string, list, or tuple. Python provides two membership operators:

- `in`
- `not in`

### 1. `in` Operator

The `in` operator returns `True` if the specified value is found in the sequence.

#### Example:
```python
# Checking if an element is in a list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True
print("orange" in fruits)  # Output: False

# Checking if a character is in a string
message = "Hello, World!"
print("H" in message)  # Output: True
print("h" in message)  # Output: False (case-sensitive)
```

### 2. `not in` Operator

The `not in` operator returns `True` if the specified value is not found in the sequence.

#### Example:
```python
# Checking if an element is not in a list
fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits)  # Output: True
print("banana" not in fruits)  # Output: False

# Checking if a substring is not in a string
message = "Hello, World!"
print("Python" not in message)  # Output: True
```

## Identity Operators

Identity operators are used to compare the memory location of two objects. They determine whether two variables refer to the same object in memory. Python provides two identity operators:

- `is`
- `is not`

### 1. `is` Operator

The `is` operator returns `True` if two variables point to the same object (i.e., have the same memory location).

#### Example:
```python
# Comparing two variables that point to the same object
a = [1, 2, 3]
b = a
print(a is b)  # Output: True

# Comparing two variables that point to different objects
c = [1, 2, 3]
print(a is c)  # Output: False
```

In the first comparison, `a` and `b` are pointing to the same list object in memory, so `a is b` returns `True`. In the second comparison, `a` and `c` point to different list objects, even though they contain the same elements, so `a is c` returns `False`.

### 2. `is not` Operator

The `is not` operator returns `True` if two variables do not point to the same object (i.e., have different memory locations).

#### Example:
```python
# Comparing two variables that do not point to the same object
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # Output: True

# Comparing two variables that point to the same object
c = a
print(a is not c)  # Output: False
```

In the first example, `a` and `b` point to different objects in memory, so `a is not b` returns `True`. In the second example, `a` and `c` point to the same object, so `a is not c` returns `False`.

## Key Differences Between `==` and `is`

- `==` compares the values of two objects to see if they are equal.
- `is` compares the identities of two objects to see if they refer to the same object in memory.

### Example:
```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # Output: True (values are equal)
print(x is y)  # Output: False (different objects in memory)
```

In this example, `x == y` returns `True` because the lists have the same elements, but `x is y` returns `False` because they are two distinct objects in memory.

---

This explanation covers the basics of membership and identity operators in Python, including their syntax, purpose, and practical examples.