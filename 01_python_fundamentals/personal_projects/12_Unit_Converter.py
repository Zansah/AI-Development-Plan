# -------------------------------------------------
# Universal Unit Converter
# -------------------------------------------------
# This program converts values between units across
# multiple categories (length, mass, time, temperature).
# The system is modular and easily extensible.
# -------------------------------------------------

def convert_temperature(value, from_unit, to_unit):
    """Handle temperature conversions separately."""
    if from_unit == "c":
        value = value if to_unit == "c" else (value * 9/5 + 32 if to_unit == "f" else value + 273.15)
    elif from_unit == "f":
        value = value if to_unit == "f" else ((value - 32) * 5/9 if to_unit == "c" else (value - 32) * 5/9 + 273.15)
    elif from_unit == "k":
        value = value if to_unit == "k" else (value - 273.15 if to_unit == "c" else (value - 273.15) * 9/5 + 32)
    return value


# Conversion tables (base unit system)
CONVERSIONS = {
    "length": {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    },
    "mass": {
        "kilogram": 1.0,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495
    },
    "time": {
        "second": 1.0,
        "minute": 60.0,
        "hour": 3600.0,
        "day": 86400.0
    }
}


def convert_units(category, value, from_unit, to_unit):
    """Convert units using base-unit normalization."""
    base_value = value * CONVERSIONS[category][from_unit]
    return base_value / CONVERSIONS[category][to_unit]


# Main program loop
while True:
    print("\nUniversal Unit Converter")
    print("Categories:")
    print("1 - Length")
    print("2 - Mass")
    print("3 - Time")
    print("4 - Temperature")
    print("5 - Quit")

    choice = input("Choose a category: ")

    if choice == "5":
        print("Converter closed.")
        break

    category_map = {"1": "length", "2": "mass", "3": "time"}

    try:
        value = float(input("Enter value: "))

        if choice == "4":
            print("Temperature units: c (Celsius), f (Fahrenheit), k (Kelvin)")
            from_unit = input("From unit: ").lower()
            to_unit = input("To unit: ").lower()
            result = convert_temperature(value, from_unit, to_unit)

        elif choice in category_map:
            category = category_map[choice]
            print(f"Available units: {', '.join(CONVERSIONS[category].keys())}")
            from_unit = input("From unit: ").lower()
            to_unit = input("To unit: ").lower()
            result = convert_units(category, value, from_unit, to_unit)

        else:
            print("Invalid category.")
            continue

        print(f"\nResult: {result:.4f}")

    except (ValueError, KeyError):
        print("Invalid input or unit.")
