
## Python provides some statements to control the flow of loops:

The continue and break statements are control flow tools in Python that allow you to alter the behavior of loops (for and while loops). They provide ways to skip iterations or exit loops prematurely based on specific conditions.

### 1. break Statement

The break statement is used to exit a loop immediately, regardless of the loop’s condition. When break is encountered, the loop terminates, and the program continues with the next statement after the loop.

***Use in a for Loop***

```
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
```

***Use in a while Loop***

```
count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break  # Exit the loop when count is 5
```


### 2. continue Statement

The continue statement is used to skip the current iteration of a loop and proceed with the next iteration. When continue is encountered, the loop doesn’t terminate; it just skips the remaining code in the current iteration and moves on to the next iteration.

***Use in a for Loop***
```
for i in range(1, 6):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print(i)

```

***Use in a while Loop***

```
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop when count is 3
    print(count)
```


When to Use break and continue:

	•	break:
	•	Exiting a loop when a certain condition is met (e.g., finding an item in a list and stopping further search).
	•	Preventing infinite loops when a certain condition occurs.
	•	continue:
	•	Skipping certain values in a loop (e.g., skipping over unwanted data or values that don’t need processing).
	•	Avoiding unnecessary computations or actions within specific loop iterations.


Both break and continue are powerful tools for managing the flow of loops, allowing you to fine-tune how and when specific blocks of code are executed.
