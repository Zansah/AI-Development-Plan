"""
LEVEL 3: Loops
"""

def numbers_1_to_10():
    """Return numbers from 1 to 10 as a list."""
    result = []
    for i in range(1, 11):
        result.append(i)
    return result


def even_numbers_1_to_50():
    """Return even numbers from 1 to 50 as a list."""
    result = []
    for i in range(1, 51):
        if i % 2 == 0:
            result.append(i)
    return result


def odd_numbers_1_to_50():
    """Return odd numbers from 1 to 50 as a list."""
    result = []
    for i in range(1, 51):
        if i % 2 != 0:
            result.append(i)
    return result


def sum_1_to_n(n):
    """Return sum of numbers from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def multiplication_table(n):
    """Return multiplication table of n as a list (1*n to 10*n)."""
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table


def count_digits(num):
    """Return number of digits in num."""
    num_abs = abs(num)
    count = 0
    while num_abs > 0:
        num_abs = num_abs // 10
        count += 1
    if count == 0:  # For num = 0
        count = 1
    return count


def reverse_number(num):
    """Return reversed number."""
    num_abs = abs(num)
    reversed_num = 0
    while num_abs > 0:
        digit = num_abs % 10
        reversed_num = reversed_num * 10 + digit
        num_abs = num_abs // 10
    if num < 0:
        reversed_num = -reversed_num
    return reversed_num


def factorial(n):
    """Return factorial of n."""
    if n < 0:
        return None  
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    pass
