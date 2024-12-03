def temperature_conversion():
    while True:
        try:
            # Ask the user for the unit (C or F)
            unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip().upper()
            
            # Ask the user for the temperature value and convert it to a float
            temperature = float(input("Enter the temperature value: "))
            
            # Check if the unit is valid
            if unit == "C":
                # Convert Celsius to Fahrenheit
                converted = (temperature * 9/5) + 32
                print(f"{temperature}°C is {converted}°F.")
            elif unit == "F":
                # Convert Fahrenheit to Celsius
                converted = (temperature - 32) * 5/9
                print(f"{temperature}°F is {converted}°C.")
            else:
                print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue  # Continue the loop if the unit is invalid

            # Ask if the user wants to continue
            another_conversion = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
            if another_conversion != "yes":
                print("Goodbye!")
                break  # Exit the loop if the user doesn't want to continue

        except ValueError:
            print("Invalid input! Please enter a valid number for the temperature.")

# Run the program
temperature_conversion()