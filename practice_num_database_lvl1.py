number_database = []

print("Welcome to the Number Database!")

while True:
    print("\nMenu:")
    print("Enter '1' to add a number to the database.")
    print("Enter '2' to view the numbers in the database.")
    print("Enter '3' to exit.")

    user_choice = input("Please enter your choice (1, 2, or 3): ")
    if user_choice == '1':
        print("Enter numbers to add to the database. Type 'stop' when you're done.")
        while True:
            user_input = input("Enter a number (or 'stop' to finish): ")
            if user_input.lower() == 'stop':
                break
            try:
                number = int(user_input)
                number_database.append(number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    elif user_choice == '2':
        if number_database:
            print("Numbers in the database:")
            for number in number_database:
                print(number)
        else:
            print("The database is currently empty.")
    elif user_choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")