# -------------------------------------------------
# Arithmetic Expression Calculator
# -------------------------------------------------
# This program repeatedly prompts the user to enter
# an arithmetic expression valdaites the input and evaluates 
# it while following the  PEMDAS rules.
# The user may choose to continue or quit after
# each calculation.
# -------------------------------------------------

# Continue running until the user chooses to quit
while True:

    # Prompt the user for an arithmetic expression
    expression = input("\nEnter an arithmetic expression: ")

    # Allowed characters for validation
    allowed_characters = "0123456789+-*/(). "

    # Validate the expression using a for loop
    is_valid = True
    for char in expression:
        if char not in allowed_characters:
            is_valid = False
            break

    # Evaluate the expression if valid
    if is_valid:
        try:
            # Evaluate expression (follows PEMDAS automatically)
            result = eval(expression)
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception:
            print("Error: Invalid arithmetic expression.")
    else:
        print("Error: Expression contains invalid characters.")

    # Ask the user whether to continue or quit
    print("\nChoose an option:")
    print("1 - Continue")
    print("2 - Quit")

    choice = input("Enter your choice: ")

    # Exit the loop if the user chooses to quit
    if choice == "2":
        print("Calculator closed.")
        break
    elif choice != "1":
        print("Invalid choice. Returning to calculator...")
