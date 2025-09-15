try:
    # Prompt the user to enter their age
    age_str = input("Please enter your age: ")

    # Convert the input string to an integer
    age = int(age_str)

    # Check if the age is within the specified range (10 to 20, inclusive)
    if 10 <= age <= 20:
        print(f"The age {age} is between 10 and 20 years.")
    else:
        print(f"The age {age} is NOT between 10 and 20 years.")

except ValueError:
    print("Invalid input. Please enter a valid whole number for age.")