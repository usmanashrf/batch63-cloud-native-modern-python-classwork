# The While Loop:

```json
while you have peanuts
    keep eating
```
- `while` and `if` both checks the conditions. If the condition is met (`True`), the instructions in `if` block exeuctures only once. However, in `while`, if the condition is met (`True`), the instructions in the `while` block runs more than once. 

- If condition evaluates to `False` the instuctions in the block never runs. 

- There should be a mechanism in the body to change the condition value. Otherwise the body will keep executing forever. 

## Situation
You have a class that runs until 6 PM. During this time, you want to keep learn Python. You don’t want to stop coding until the clock hits 6 PM.


In a real-life scenario, you might keep checking the time every few minutes while you’re coding to see if it’s 6 PM yet:

	1.	Start coding.
	2.	Check the time.
	3.	If it’s not 6 PM, continue coding.
	4.	Repeat this process until it’s 6 PM.

This approach works, but it requires constant attention to the clock, which can be distracting.

# While Loop
The while loop in Python is a control flow statement that allows code to be executed repeatedly based on a given condition. The loop continues to execute as long as the condition evaluates to True. Once the condition becomes False, the loop stops running.

#### syntax
```
while condition:
    # Code block to be executed repeatedly
```

In a programming context, you can automate this process using a while loop that will allow you to keep coding until the time reaches 6 PM.

```
while current_time < 18:  # 18 represents 6 PM in 24-hour format
    print("Still coding... The time is not yet 6 PM.")

print("It's 6 PM! Time to stop coding and end the class.")
```

---

### Example 1: Basic while Loop

```
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```
Explanation:

	•	The loop starts with count equal to 0.
	•	It prints the value of count and then increments count by 1.
	•	This process repeats until count is no longer less than 5.


### Example 2: while Loop with a Condition
You can use a while loop to keep prompting the user until they enter a valid input.

```
password = ""
while password != "Pass123":
    password = input("Enter the password: ")

print("Access granted")
```


### Example 3: Infinite while Loop
A while loop can run indefinitely if the condition never becomes False. This is known as an infinite loop, and it will continue to run until you manually stop it or break out of it with a break statement.

```
while True:
    print("This loop will run forever")
    # You can include a break condition to exit the loop
```

***Note: Be careful with infinite loops, as they can cause your program to hang if not properly managed.***


