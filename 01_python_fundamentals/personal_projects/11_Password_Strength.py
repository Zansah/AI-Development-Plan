# -------------------------------------------------
# Password Strength Checker
# -------------------------------------------------
# This program evaluates password strength based on
# industry-standard criteria:
# - Length
# - Uppercase & lowercase letters
# - Numbers
# - Special characters
# - Common password patterns
# -------------------------------------------------

import string


def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Character type checks
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Common password checks
    common_patterns = ["123", "password", "admin", "qwerty"]
    lower_pass = password.lower()

    for pattern in common_patterns:
        if pattern in lower_pass:
            feedback.append("Avoid common password patterns.")
            score -= 1
            break

    # Strength evaluation
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


# Main program loop
while True:
    password = input("\nEnter a password to evaluate (or type 'quit' to exit): ")

    if password.lower() == "quit":
        print("Password checker closed.")
        break

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print("-", tip)
    else:
        print("Your password meets all recommended security criteria.")
