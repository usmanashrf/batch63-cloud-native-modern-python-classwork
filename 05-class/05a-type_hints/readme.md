# Type Hinting in Python

## Overview

Type hinting is a feature introduced in Python 3.5 that allows to indicate the expected data types of variables, function arguments, and return values. While Python is a dynamically typed language, type hints provide additional context that can help with code readability, debugging, and development in large codebases.

## Benefits of Type Hinting

- **Improved Readability**: Type hints make it clear what types of values are expected and returned by functions, making the code easier to understand.
- **Enhanced IDE Support**: Many IDEs and editors can use type hints to provide better autocompletion, inline documentation, and error checking.
- **Static Analysis**: Tools like `mypy` can analyze code for type inconsistencies without running the program, helping to catch potential bugs early.

## Basic Usage

### Variables

We can use type hints when declaring variables:

```python
name: str = "Alice"
age: int = 30
height: float = 1.75
is_active: bool = True
```
