#!/usr/bin/env python3
"""
This module contains classes representing CountedIterator.
"""
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
        else:
            print(f"Item {item} not found in the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            popped_item = super().pop()
            print(f"Popped {popped_item} from the list.")
            return popped_item
        else:
            popped_item = super().pop(index)
            print(f"Popped {popped_item} from the list.")
            return popped_item
