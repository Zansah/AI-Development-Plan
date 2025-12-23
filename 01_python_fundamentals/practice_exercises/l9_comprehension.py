"""
LEVEL 9: List Comprehensions & Lambdas
"""

def squares():
    """Return squares from 1 to 10."""
    result = []
    for i in range(1, 11):
        square = i * i
        result.append(square)
    return result


def even_numbers(nums):
    """Return even numbers from list."""
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result


def uppercase_strings(words):
    """Convert list of strings to uppercase."""
    result = []
    for word in words:
        upper_word = word.upper()
        result.append(upper_word)
    return result


def numbers_greater_than_50(nums):
    """Return numbers greater than 50."""
    result = []
    for num in nums:
        if num > 50:
            result.append(num)
    return result


def double_numbers(nums):
    """Double numbers (expanded version of map)."""
    result = []
    for num in nums:
        doubled = num * 2
        result.append(doubled)
    return result


def remove_odds(nums):
    """Remove odd numbers (expanded version of filter)."""
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result


