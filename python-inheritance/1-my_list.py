#!/usr/bin/python3

class MyList(list):
    """A subclass of list that includes a method to print the list
        sorted in ascending order."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
