# -------------------------------------------------
# Multiplication Table Generator
# -------------------------------------------------
# This program prompts the user to enter a number
# and displays a formatted multiplication table
# from 1 to 10. Input validation is included to
# ensure correct user input.
# -------------------------------------------------

while True:
    try:
        # Prompt the user for a number
        number = int(input("\nEnter a number for the multiplication table: "))

        # Display table header
        print("\nMultiplication Table for", number)
        print("-" * 30)

        # Generate and display the multiplication table
        for i in range(1, 13):
            print(f"{number:>3} x {i:>2} = {number * i:>4}")

    except ValueError:
        # Handle non-integer input
        print("Error: Please enter a valid integer.")
        continue

    print("\nChoose an option:")
    print("1 - Generate another table")
    print("2 - Quit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("Program ended.")
        break
    elif choice != "1":
        print("Invalid choice. Returning to menu...")
