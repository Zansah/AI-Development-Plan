"""
LEVEL 5: Lists
Practice list operations and algorithms.
"""

def sum_of_list(nums):
    """Return the sum of all elements in a list."""
    total = 0
    for num in nums:
        total += num
    return total


def max_and_min(nums):
    """Return the maximum and minimum values in a list."""
    if len(nums) == 0:
        return None

    maximum = nums[0]
    minimum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


def count_even_odd(nums):
    """Return the count of even and odd numbers."""
    even_count = 0
    odd_count = 0

    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


def remove_duplicates(nums):
    """Return a list with duplicates removed."""
    unique = []

    for num in nums:
        if num not in unique:
            unique.append(num)

    return unique


def sort_list(nums):
    """Sort a list without using built-in sort()."""
    sorted_list = nums.copy()
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp

    return sorted_list


def second_largest(nums):
    """Return the second largest number."""
    if len(nums) < 2:
        return None

    largest = nums[0]
    second = None

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num != largest:
            if second is None or num > second:
                second = num

    return second


def rotate_list(nums, k):
    """Rotate list by k positions to the right."""
    n = len(nums)
    if n == 0:
        return nums

    k = k % n
    rotated = []

    for i in range(n - k, n):
        rotated.append(nums[i])

    for i in range(0, n - k):
        rotated.append(nums[i])

    return rotated


def common_elements(a, b):
    """Return common elements between two lists."""
    common = []

    for item in a:
        if item in b and item not in common:
            common.append(item)

    return common

