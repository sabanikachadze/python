def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value  # Return the valid input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_numbers(amount):
    total_sum = 0

    for _ in range(amount):
        while True:
            try:
                number = int(input("Enter a positive number: "))
                if number < 0:
                    print("Please enter a positive number.")
                else:
                    total_sum += number
                    break  # Exit inner loop on valid input
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return total_sum

def main():
    amount = get_positive_integer("How many positive numbers do you want to enter? ")
    total_sum = get_valid_numbers(amount)
    average = total_sum / amount
    print(f"The average of the numbers is: {average:.2f}")
        
        


if __name__ == "__main__":
    main()