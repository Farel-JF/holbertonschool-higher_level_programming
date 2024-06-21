#!/usr/bin/env python3
""" VerboseList extends Python list"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        if item in self:
            print("Removed {} from the list.".format(item))
        else:
            print("Item {} not found in the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            _item = super().pop()
            print("Popped {} from the list.".format(_item))
            return _item
        else:
            _item = super().pop(index)
            print("Popped {} from the list.".format(_item))
            return _item
