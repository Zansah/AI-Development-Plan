"""
LEVEL 7: Dictionaries
"""

def print_dictionary(d):
    """Print all key-value pairs."""
    for key in d:
        print(key, ":", d[key])


def word_frequency(sentence):
    """Return frequency of each word."""
    freq = {}
    words = sentence.split()

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def max_value_key(d):
    """Return key with maximum value."""
    if len(d) == 0:
        return None

    max_key = None
    max_value = None

    for key in d:
        if max_value is None or d[key] > max_value:
            max_value = d[key]
            max_key = key

    return max_key


def merge_dictionaries(d1, d2):
    """Merge two dictionaries."""
    merged = {}

    for key in d1:
        merged[key] = d1[key]

    for key in d2:
        merged[key] = d2[key]  # overwrites if key exists

    return merged


def key_exists(d, key):
    """Check if key exists in dictionary."""
    for k in d:
        if k == key:
            return True
    return False


def sort_by_keys(d):
    """Return dictionary sorted by keys."""
    sorted_dict = {}
    keys = list(d.keys())

    # simple bubble sort on keys
    n = len(keys)
    for i in range(n):
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                temp = keys[j]
                keys[j] = keys[j + 1]
                keys[j + 1] = temp

    for key in keys:
        sorted_dict[key] = d[key]

    return sorted_dict


def sort_by_values(d):
    """Return dictionary sorted by values."""
    sorted_dict = {}
    items = list(d.items())
    n = len(items)

    # bubble sort by value
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp

    for key, value in items:
        sorted_dict[key] = value

    return sorted_dict

