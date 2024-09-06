# Recursive Functions in Python

Functions in Python are powerful tools for structuring programs, and **recursive functions** offer even more flexibility.

## What is Recursion?

**Recursion** is a programming technique where a function calls itself to solve a problem. The key idea is that the problem is broken down into smaller sub-problems, and the function continues calling itself with simpler inputs until it reaches a base case (a stopping condition).

### Key Points:

- Every recursive function has a **base case** to terminate the recursion.

- A recursive function solves a problem by reducing it to a smaller version of itself.

---

## Examples of Recursive Functions

### Example 1: Factorial Calculation

The **factorial** of a number `n` is the product of all positive integers less than or equal to `n`. Factorials can be defined recursively, where `n! = n * (n-1)!` and the base case is `0! = 1`.

**Without Recursion**

```python
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result *= i
        return result
print(factorial(5)) # Output: 120

```

**With Recursion**

```python
def factorial(n):
    # Base case
    if n < 0:
        return None
    if n < 2:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Example 2: Fibonacci Sequence

The **Fibonacci sequence** is a series where each number is the sum of the two preceding ones. The recursive relation is `F(n) = F(n-1) + F(n-2)` with the base cases `F(0) = 0` and `F(1) = 1`.

**Without Recursion**

```python
def fibbonacci (n):
    if n < 0:
        return None
    if n < 3:
        return 1
    else:
        e1 = e2 = 1
        sum = 0
        for i in range(3, n+1):
            sum = e1 + e2
            e1, e2 = e2, sum
        return sum
print (fibbonacci(6))

```

**With Recursion**

```python
def fibbonacci (n):
    if n < 0:
        return None
    if n < 3:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)
print (fibbonacci(6))
```

## Key Notes

- If you forget to consider the conditions which can stop the
  chain of recursive invocations, the program may enter an infinite loop.
- Recursive calls consume a lot of memory and therefore recursive functions may sometimes
  be inefficient.
