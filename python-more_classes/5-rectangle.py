#!/usr/bin/python3
"""Rectangle"""

class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height.

        Args:
            width (int, optional): The width of the rectangle.
            Defaults to 0.
            height (int, optional): The height of the rectangle.
            Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """Return a string representation of the rectangle with
        the character #.

        Returns:
            str: The rectangle represented with the character #.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of the rectangle to recreate a
        new instance.

        Returns:
            str: The string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
