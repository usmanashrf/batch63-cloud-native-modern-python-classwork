condition = ""
while condition != 'exit':
    user_in = input("Enter command: ")
    if user_in != 'exit':
        print(user_in)
    elif user_in == 'exit':
        condition = user_in