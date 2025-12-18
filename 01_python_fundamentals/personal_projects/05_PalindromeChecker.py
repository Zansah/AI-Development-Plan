# -----------------------------------------
# Palindrome Checker Program
# -----------------------------------------
# This program checks whether a word or
# sentence is a palindrome.
# It ignores spaces, punctuation, and case.
# -----------------------------------------

while True:
    # Ask the user for input
    text = input("Enter a word or sentence: ")

    # Clean the text:
    # - keep only letters and numbers
    # - convert to lowercase
    cleaned_text = ""
    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()

    # Reverse the cleaned text
    reversed_text = cleaned_text[::-1]

    # Check if palindrome
    if cleaned_text == reversed_text:
        print("This is a palindrome!")
    else:
        print("This is NOT a palindrome.")

    # Ask if the user wants to continue
    print("\n1. Check another word/sentence")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("Goodbye!")
        break

    print("\n-----------------------------\n")
