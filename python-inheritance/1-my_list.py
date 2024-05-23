#!/usr/bin/python3
"""Definition of function my_list"""


class MyList(list):
    """A subclass of list that includes a method to print the list
        sorted in ascending order."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        for element in self:
            if not isinstance(element, int):
                raise TypeError("not all the elements type int")
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
