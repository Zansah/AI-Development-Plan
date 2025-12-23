"""
LEVEL 6: Tuples & Sets
"""

def tuple_length(t):
    """Return the length of a tuple."""
    count = 0
    for _ in t:
        count += 1
    return count


def tuple_contains(t, item):
    """Check if item exists in tuple."""
    for element in t:
        if element == item:
            return True
    return False


def remove_duplicates_set(nums):
    """Remove duplicates using a set."""
    unique_set = set()
    for num in nums:
        unique_set.add(num)
    return unique_set


def set_union(a, b):
    """Return union of two sets."""
    result = set()

    for item in a:
        result.add(item)

    for item in b:
        result.add(item)

    return result


def set_intersection(a, b):
    """Return intersection of two sets."""
    result = set()

    for item in a:
        if item in b:
            result.add(item)

    return result


def set_difference(a, b):
    """Return difference of two sets (items in a not in b)."""
    result = set()

    for item in a:
        if item not in b:
            result.add(item)

    return result


def is_subset(a, b):
    """Check if set a is subset of set b."""
    for item in a:
        if item not in b:
            return False
    return True
