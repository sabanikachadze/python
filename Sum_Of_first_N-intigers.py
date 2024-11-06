sum = 0

while True:
    try:
        num = int(input("Enter Number: "))
        
        if num < 0:
            print("Number must not be negative!")
            continue  # Go back to the start of the loop if the input is negative
        
        # Reset sum for each valid input
        sum = 0
        for n in range(num + 1):
            sum += n
            
        print("Sum of numbers from 0 to", num, "is:", sum)
        
        break  # Exit the loop after a successful calculation

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
