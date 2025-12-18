# -----------------------------------------
# Number Checker Program
# -----------------------------------------
# This program asks the user for a number
# and checks:
# 1. Positive / Negative / Zero
# 2. Even or Odd
# 3. Prime or Not Prime
# -----------------------------------------

while True:
    # Ask the user for a number
    num = int(input("Enter an integer: "))

    # Check if positive, negative, or zero
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    # Check if even or odd
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    # Check if the number is prime
    if num <= 1:
        print("The number is not prime.")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("The number is prime.")
        else:
            print("The number is not prime.")

    # Ask if the user wants to continue
    print("\n1. Check another number")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("Goodbye!")
        break

    print("\n-----------------------------\n")
