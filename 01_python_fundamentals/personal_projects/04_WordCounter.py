# -----------------------------------------
# Word Counter Program
# -----------------------------------------
# This program:
# 1. Counts the number of words
# 2. Counts the number of characters
# 3. Counts characters without spaces
# 4. Counts sentences
# -----------------------------------------

while True:
    # Ask the user for text input
    text = input("Enter your text: ")

    # Remove leading/trailing spaces and split by spaces
    words = text.strip().split()

    # Count words
    word_count = len(words)

    # Count characters (including spaces)
    char_count = len(text)

    # Count characters (excluding spaces)
    char_no_space = len(text.replace(" ", ""))

    # Count sentences (basic approach)
    sentence_count = 0
    for char in text:
        if char in ".!?":
            sentence_count += 1

    # Display results
    print("\n--- Word Counter Results ---")
    print(f"Words: {word_count}")
    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (no spaces): {char_no_space}")
    print(f"Sentences: {sentence_count}")

    # Ask the user if they want to continue
    print("\n1. Count another text")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("Goodbye!")
        break

    print("\n-----------------------------\n")
