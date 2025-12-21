"""
LEVEL 2: Conditionals
"""

def is_even_or_odd(num):
    """Return 'Even' or 'Odd'."""
    # TODO: check parity
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def divisible_by_3_and_5(num):
    """Check if number is divisible by both 3 and 5."""
    # TODO: check divisibility
    if num % 3 == 0 and num % 5 == 0:
        return True


def largest_of_two(a, b):
    """Return the larger of two numbers."""
    # TODO: compare numbers
    largest = max(a,b)
    return largest


def largest_of_three(a, b, c):
    """Return the largest of three numbers."""
    # TODO: determine largest
    largest = max(a, b, c)
    return largest


def is_leap_year(year):
    """Check if year is a leap year."""
    # TODO: leap year logic
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def assign_grade(score):
    """Return letter grade based on score."""
    # TODO: assign grade using conditions
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_vowel(char):
    """Check if character is a vowel."""
    # TODO: check vowel
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True
    else:
        return False


def in_range(num, start, end):
    """Check if number is within range."""
    # TODO: range check
    return start <= num <= end


def ticket_price(age):
    """Return ticket price based on age."""
    # TODO: apply age pricing
    if age <= 12:
        return 5
    elif age <= 64:
        return 10
    else:
        return 7


def valid_password(password):
    """Check if password length is at least 8."""
    # TODO: validate password length
    return len(password) >= 8
