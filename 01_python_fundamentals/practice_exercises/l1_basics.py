"""
LEVEL 1: Basics & Syntax
"""

def print_hello_world():
    """Print 'Hello, World!'."""
    # TODO: print Hello, World!
    print("Hello, World!")


def print_name_and_age(name, age):
    """Print name and age on separate lines."""
    # TODO: print name
    # TODO: print age
    name = name
    age = age
    print(f"{name} \n {age}")


def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    # TODO: return sum
    return a + b


def subtract_two_numbers(a, b):
    """Return the difference of two numbers."""
    # TODO: return difference
    return a - b


def multiply_two_numbers(a, b):
    """Return the product of two numbers."""
    # TODO: return product
    return a * b


def divide_two_numbers(a, b):
    """Return the quotient of two numbers."""
    # TODO: return quotient
    return a // b


def swap_variables(a, b):
    """Return swapped values of a and b."""
    a, b = b, a
    return a, b




def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # TODO: apply conversion formula
    return (celsius * 9/5) + 32


def minutes_to_hours(minutes):
    """Convert minutes to (hours, remaining minutes)."""
    # TODO: calculate hours
    # TODO: ca
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

if __name__ == "__main__":
    print_hello_world()
    print_name_and_age("Elise", 20)