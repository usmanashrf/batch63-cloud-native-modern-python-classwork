## The Problem:

Imagine you’re organizing a birthday party and you want to send an invitation message to 50 of your friends. Without any tools or shortcuts, you would have to write the same message 50 times, changing only the name of each friend. This is repetitive and time-consuming.

you would have to manually send each message like this:

```
print("Hi Alice, you’re invited to my birthday party!")
print("Hi Bob, you’re invited to my birthday party!")
print("Hi Charlie, you’re invited to my birthday party!")
# ...and so on, for 50 friends
```

If you have a long list of friends, this approach quickly becomes impractical. Not only does it take a lot of time, but if you want to change the message later, you’d have to edit each line individually.

## The Solution: Using Loops to Automate Invitations

Now, let’s say you want to automate this process. You can use a loop to send the same message to all your friends with just a few lines of code

```
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]  # and so on, up to 50 names

for friend in friends:
    print(f"Hi {friend}, you’re invited to my birthday party!")

```

