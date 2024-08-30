# Introduction to Tuples in Python
A sequence is a type of data in python which is able to store more than one value. These values can be sequentially browsed i.e. element by element. 

So far, we've only studied one type of sequence i.e. `list`. Here we'll explore another type of sequene called `tuple`. 

We've already discussed the concept of **Immutability** and **Mutability**. Let's revise it. 

- *Immutabale* means can't be changed/modified/updated. Example: Primitive Data types
- *Mutable* means can be changed/modified/updated. Example: Lists in Python


## What is a Tuple?

A tuple is an immutable, ordered collection of elements in Python. Like lists, tuples can hold a sequence of elements, but unlike lists, tuples cannot be changed (i.e., modified) after they are created. Tuples are typically used to group together related data.

## Why Do We Need Tuples?
### The Problem: Need for Immutable Collections

In programming, there are situations where we want to ensure that a sequence of values remains constant throughout the program. For example, we might have a set of coordinates or configuration values that should not be altered accidentally.

Using a list for such cases is risky because lists are mutable, meaning their content can be changed. This is where tuples come in handy.

### The Solution: Using Tuples for Immutable Sequences

Tuples provide a way to create a sequence of elements that cannot be modified. This immutability makes tuples useful in scenarios where the integrity of the data must be preserved.

```python
coordinates : tuple[int,int] = (10, 20)
print(coordinates)  # Output: (10, 20)

# Trying to modify a tuple will raise an error
# coordinates[0] = 15  # This will raise a TypeError
```

## How Tuples Work

### Basic Syntax

Tuples are created by placing a sequence of elements separated by commas within parentheses:

```python
my_tuple : tuple[int, int, int] = (1, 2, 3)
```

### Example: Storing Multiple Values

Tuples can be used to store related data, such as the x, y, and z coordinates of a point in space:

```python
point : tuple[int, int, int] = (1, 2, 3)
print(point)  # Output: (1, 2, 3)
```

### Creating a Tuple Without Parentheses

We can also create a tuple without using parentheses by simply separating the elements with commas:

```python
my_tuple : tuple[int, int, int] = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)
```

### Single-Element Tuples

To create a tuple with a single element, we must include a trailing comma:

```python
single_element_tuple = (5,)
print(single_element_tuple)  # Output: (5,)
```

Without the comma, Python will not recognize it as a tuple:

```python
not_a_tuple = (5)
print(type(not_a_tuple))  # Output: <class 'int'>
```

## Operations with Tuples

### Accessing Elements

We can access elements in a tuple using indexing, similar to lists:

```python
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[1])  # Output: banana
```

### Slicing Tuples

We can slice tuples to get a range of elements:

```python
my_tuple = ('apple', 'banana', 'cherry', 'date')
print(my_tuple[1:3])  # Output: ('banana', 'cherry')
```

### Tuple Concatenation and Repetition

Tuples can be concatenated using the `+` operator and repeated using the `*` operator:

```python
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)

# Repetition
repeated_tuple = ('A',) * 3
print(repeated_tuple)  # Output: ('A', 'A', 'A')
```

### Tuple Unpacking

Tuple unpacking allows us to assign each element of a tuple to a variable in a single statement:

```python
scores = (10, 20)
x, y = scores
print(x)  # Output: 10
print(y)  # Output: 20
```

### Nesting Tuples

Tuples can contain other tuples, which is useful for organizing data hierarchically:

```python
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5, 6))
```

## Advantages of Tuples

### 1. Immutability

The immutability of tuples ensures that the data remains consistent and secure, especially in cases where the data should not be altered.

### 2. Performance

Tuples are generally faster than lists for iterating through elements because they are immutable and therefore require less memory.

### 3. Use as Dictionary Keys

Because tuples are immutable, they can be used as keys in dictionaries, unlike lists.

```python
location = {}
point = (10, 20)
location[point] = "Park"
print(location)  # Output: {(10, 20): 'Park'}
```

## Conclusion

Tuples are a fundamental data structure in Python that provide a way to store ordered, immutable collections of elements. They are ideal for situations where we need a sequence of elements that should not be changed, and they offer several advantages in terms of performance and data integrity.


## Tuple Methods and Operations

### 1. `count()`

The `count()` method returns the number of occurrences of a specified value in the tuple.

#### Example:

```python
my_tuple = (1, 2, 3, 2, 2, 4)
count_of_twos = my_tuple.count(2)
print(count_of_twos)  # Output: 3
```

### 2. `index()`

The `index()` method returns the index of the first occurrence of a specified value. If the value is not found, it raises a `ValueError`.

#### Example:

```python
my_tuple = ('apple', 'banana', 'cherry')
index_of_banana = my_tuple.index('banana')
print(index_of_banana)  # Output: 1
```

### Tuple Operations

#### 1. Accessing Elements

We can access elements of a tuple using square brackets `[]` with the index of the element. Remember that tuple indices start at 0.

```python
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[0])  # Output: apple
```

#### 2. Slicing

We can slice a tuple to get a subset of elements:

```python
my_tuple = ('apple', 'banana', 'cherry', 'date')
print(my_tuple[1:3])  # Output: ('banana', 'cherry')
```

#### 3. Concatenation

Tuples can be concatenated using the `+` operator:

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
```

#### 4. Repetition

We can repeat a tuple a certain number of times using the `*` operator:

```python
my_tuple = ('A', 'B')
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: ('A', 'B', 'A', 'B', 'A', 'B')
```

#### 5. Membership Test

We can check if an item exists in a tuple using the `in` keyword:

```python
my_tuple = ('apple', 'banana', 'cherry')
print('banana' in my_tuple)  # Output: True
print('grape' in my_tuple)   # Output: False
```

#### 6. Iterating Over a Tuple

We can iterate over the elements of a tuple using a `for` loop:

```python
my_tuple = ('apple', 'banana', 'cherry')
for fruit in my_tuple:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

### Tuple Usage Examples


#### 1. Swapping Variables

Tuples can be used for swapping the values of two variables without needing a temporary variable.

```python
a = 5
b = 10
a, b = b, a
print(a)  # Output: 10
print(b)  # Output: 5
```
#### 2. Swapping Tuples
Tuples themselves can be swapped.

```python
t1 = (1,2)
t2 = (2,3)
print(f"Before swapping: t1={t1} and t2={t2}") # Output: Before swapping: t1=(1, 2) and t2=(2, 3)
t1, t2 = t2, t1
print(f"After swapping: t1={t1} and t2={t2}") # Output: After swapping: t1=(2, 3) and t2=(1, 2)
```

#### 3. Storing Related Data

Tuples can store related data, like coordinates or RGB color values.

```python
point = (10, 20)
color = (255, 0, 0)

print(point)  # Output: (10, 20)
print(color)  # Output: (255, 0, 0)
```

#### 4. Using Tuples as Dictionary Keys

Because tuples are immutable, they can be used as keys in dictionaries.

```python
locations = {}
point = (10, 20)
locations[point] = "Park"
print(locations)  # Output: {(10, 20): 'Park'}
```


