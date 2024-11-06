while True:
    try:
        first_number = float(input("Choose First Number: "))
        second_number = float(input("Choose Second Number: "))
        operator = input("Write any operator (+, -, *, /): ")

        if operator == "+":
            result = first_number + second_number
            print(f"The result is: {result}")

        elif operator == "-":
            result = first_number - second_number
            print(f"The result is: {result}")

        elif operator == "*":
            result = first_number * second_number
            print(f"The result is: {result}")

        elif operator == "/":
            if second_number != 0:
                result = first_number / second_number
                print(f"The result is: {result}")
            else:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid operator. Please choose one of +, -, *, or /.") 
            continue  # go to the next iteration if the operator is invalid

        # Optional: ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Thank you for using the calculator. Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number. iyo d aaa iyo ra ")