#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a Roman numeral string to an integer.

    Args:
        roman_string (str): The input Roman numeral string.

    Returns:
        int: The integer value corresponding to the Roman numeral string.
    """

    if not roman_string or None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_numerals[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
