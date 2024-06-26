#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: The first integer.
        b: The second integer, defaulting to 98.

    Returns:
        The sum of a and b, both casted to integers if they are floats.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
