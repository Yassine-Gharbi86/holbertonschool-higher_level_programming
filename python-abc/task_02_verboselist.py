#!/usr/bin/env python3
"""Module that defines a class VerboseList extending the built-in list class."""


class VerboseList(list):
    """A class named VerboseList extending the built-in list class."""

    def append(self, item):
        """Appends an item to the list and prints a notification message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with elements from the iterable and prints a notification message."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes the first occurrence of the item from the list and prints a notification message."""
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """Pops the item at the given index from the list and prints a notification message."""
        if -len(self) <= index < len(self):
            item = self[index]
            print(f"Popped [{item}] from the list.")
            return super().pop(index)
        else:
            print(f"Index [{index}] out of range.")
            raise IndexError("pop index out of range")
