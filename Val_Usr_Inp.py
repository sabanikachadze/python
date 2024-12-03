def Validate_input():
    print("\nUser name Can't be longer than 12 characters.\nIt must have zero spaces. \nAnd no digites!!")           
    while True:
        try:
            user_name = input("Write your username here:")
            
            if len(user_name) > 12:
                print("Don't exceed the 12 Character limit.")
                continue
            elif user_name.find(" ") != -1:
                print("Don't Include any spaces.")
                print(len(user_name))
                continue
            elif not user_name.isalpha():
                print("Don't Include any digits.")
                continue
            else:
                print(f"\nYour usarname is valid! : {user_name}")   
            another_conversion = input("Do you want to Validate your username again? (yes/no): ").strip().lower()
            if another_conversion != "yes":
                print("Goodbye!")
                break  # Exit the loop if the user doesn't want to continue

        except ValueError:
            print("Invalid input! Please enter a valid number characters.")

# Run the program
Validate_input()