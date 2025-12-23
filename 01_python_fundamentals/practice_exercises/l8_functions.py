"""
LEVEL 8: Functions
"""

def add(a, b):
    """Return sum of two numbers."""
    result = a + b
    return result


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def factorial(n):
    """Return factorial of a number."""
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result


def reverse_string(s):
    """Return reversed string."""
    reversed_str = ""
    index = len(s) - 1

    while index >= 0:
        reversed_str += s[index]
        index -= 1

    return reversed_str


def list_max(nums):
    """Return max value from list."""
    if len(nums) == 0:
        return None

    maximum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


def average(nums):
    """Return average of numbers."""
    if len(nums) == 0:
        return None

    total = 0
    count = 0

    for num in nums:
        total += num
        count += 1

    return total / count


def fibonacci(n):
    """Return nth Fibonacci number."""
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(2, n + 1):
        next_val = prev + curr
        prev = curr
        curr = next_val

    return curr
