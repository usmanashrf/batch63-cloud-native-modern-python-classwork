# Introduction to Dictionaries in Python

## What is a Dictionary?

Dictionary, a data structure in Python, is a collection of *key-value pairs*, where each *key is unique*, and each key is associated with a specific value. Unlike other data structures in Python, like lists or sets, *dictionaries are unordered*, meaning that the items are not stored in any particular sequence.

Dictionary enable the association of values with unique keys, providing a way to store and retrieve information using meaningful identifiers. Dictionaries are particularly valuable when there is a need for fast data access and retrieval based on specific keys. They are versatile and widely used in scenarios where data needs to be stored and accessed in a structured manner.

## Why Do We Need Dictionaries?

### The Problem: Efficient Data Lookups

Consider a scenario where 're managing a collection of student scores in different subjects. Initially,  might think of using two separate lists—one for student names and one for their corresponding scores:

```python
students : list[str ]= ["Alice", "Bob", "Charlie"]
scores : list[int] = [85, 92, 78]
```

To find the score of a specific student,  would need to first find the index of the student's name in the `students` list and then use that index to look up the score in the `scores` list:

```python
index : int = students.index("Alice")
score : int = scores[index]
```

While this approach works, it quickly becomes inefficient as the lists grow in size. Searching for a student's name in the list takes time, and managing two separate lists can lead to errors, especially if they become out of sync.

### The Solution: Constant-Time Lookups with Dictionaries

Dictionaries provide a more efficient and intuitive way to handle this situation. By using student names as keys and their scores as values,  can store the data in a dictionary:

```python
students_scores : dict{str,int} = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
```

Now, finding a student's score is much simpler and faster:

```python
score : int = students_scores["Alice"]
```

This operation is performed in constant time, regardless of the number of students.

## What Problems Do Dictionaries Solve?

### 1. Fast Data Retrieval

Dictionaries are optimized for fast data retrieval. Instead of searching through an entire list,  can quickly access any value directly by its key.

### 2. Clearer, More Expressive Code

Dictionaries allow us to write clearer and more expressive code. The key-value structure makes it obvious what each item represents, improving code readability.

### 3. Flexibility in Data Organization

Dictionaries offer flexibility in how  organize data.  can store complex structures, like lists or other dictionaries, as values, enabling us to represent nested or hierarchical data.

## Working with Dictionaries in Python

### Important Properties
- Each key should be unique
- Key can be any immutable type of object
- `len()` function also works with dictionaries i.e. returns the length of key-value pairs
- A dictionary is a one way tool i.e. We can find the value from key but cannot find they key from value. It works the same way as original dictionary.We can find urdu menaing of word in english but not the english meaning of urdu word.
- The dictionaries are not ordered. We might have different orders when we use `print()` function.
- Dictionaries are not a sequence type. So can we use for loop with dictionaries? No! and Yes! We'll see it in below examples. 

### Creating a Dictionary

 can create a dictionary using curly braces `{}` or the `dict()` function.

#### Example:
```python
# Using curly braces
student_scores : dict[str, int] = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Using dict() function
student_scores : dict[str,int] = dict(Alice=85, Bob=92, Charlie=78)
```

### Accessing Values

 can access values in a dictionary using the key inside square brackets `[]` or with the `.get()` method.

#### Example:
```python
# Accessing a value using a key
print(student_scores["Alice"])  # Output: 85

# Using the get() method
print(student_scores.get("Bob"))  # Output: 92
```

#### Handling Missing Keys
The `.get()` method is safer for accessing keys, as it returns `None` or a default value if the key is not found, rather than raising a `KeyError`.

#### Example:
```python
# Using square brackets (raises KeyError if key is not found)
# print(student_scores["David"])  # Uncommenting this line would raise KeyError

# Using get() (returns None if key is not found)
print(student_scores.get("David"))  # Output: None

# Providing a default value with get()
print(student_scores.get("David", "Not Found"))  # Output: Not Found
```

## Adding and Updating Items

 can add a new key-value pair or update an existing one using square brackets `[]`.

#### Example:
```python
# Adding a new key-value pair
student_scores["David"] = 88
print(student_scores)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88}

# Updating an existing key-value pair
student_scores["Alice"] = 90
print(student_scores)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88}

```

### Removing Items

 can remove items using the `del` statement, the `.pop()` method, or the `.popitem()` method.

#### Example:
```python
# Removing a specific key-value pair using del
del student_scores["Charlie"]
print(student_scores)  # Output: {'Alice': 90, 'Bob': 92, 'David': 88}

# Removing a specific key-value pair using pop()
removed_score = student_scores.pop("David")
print(removed_score)  # Output: 88
print(student_scores)  # Output: {'Alice': 90, 'Bob': 92}

# Removing the last inserted key-value pair using popitem()
last_item = student_scores.popitem()
print(last_item)  # Output: ('Bob', 92)
print(student_scores)  # Output: {'Alice': 90}
```

## Checking if a Key Exists

 can check if a key exists in a dictionary using the `in` keyword.

#### Example:
```python
print("Alice" in student_scores)  # Output: True
print("Charlie" in student_scores)  # Output: False
```

### Iterating Through a Dictionary

We can iterate through the keys, values, or key-value pairs in a dictionary using a `for` loop.

#### Example:
```python
# Iterating through keys
for student in student_scores:
    print(student)
# Output:
# Alice

# Iterating through values
for score in student_scores.values():
    print(score)
# Output:
# 90

# Iterating through key-value pairs
for student, score in student_scores.items():
    print(f"{student}: {score}")
# Output:
# Alice: 90
```

### Dictionary Methods

#### 1. `.keys()` Method
Returns a view object that displays a list of all the keys in the dictionary.

*Example:*
```python
keys = student_scores.keys()
print(keys)  # Output: dict_keys(['Alice'])
```

#### 2. `.values()` Method
Returns a view object that displays a list of all the values in the dictionary.

*Example:*
```python
values = student_scores.values()
print(values)  # Output: dict_values([90])
```

#### 3. `.items()` Method
Returns a view object that displays a list of the dictionary’s key-value tuple pairs.

*Example:*
```python
items = student_scores.items()
print(items)  # Output: dict_items([('Alice', 90)])
```

#### 4. `.update()` Method
Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.

*Example:*
```python
additional_scores = {"Eve": 95, "Frank": 87}
student_scores.update(additional_scores)
print(student_scores)  # Output: {'Alice': 90, 'Eve': 95, 'Frank': 87}
```

#### 5. `.clear()` Method
Removes all items from the dictionary.

*Example:*
```python
student_scores.clear()
print(student_scores)  # Output: {}
```

#### 5. `.copy()` Method
Removes all items from the dictionary.

*Example:*
```python
sutdent_scroes_copy = student_scores.copy()
print(sutdent_scroes_copy)  # Output: {}
```

### Dictionary Comprehension
We can also apply comprehension method on dictionaries. 

*Example:*
```python
values : dict[int,int] = {x:x for x in range(5)}
print(values)  # Output: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
```

*Example:*
```python
fruits : list[str] = ["apple", "banana", "orange"]
fruits_dict : dict[int,str] = {i:fruit for i, fruit in enumerate(fruits)}
print(fruits_dict)  # Output: {0: 'apple', 1: 'banana', 2: 'orange'}
```