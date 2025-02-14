#!/usr/bin/env python3
"""Module that defines a class CountedIterator
extending the built-in iterator."""


class CountedIterator:
    """A class named CountedIterator extending the built-in iterator."""

    def __init__(self, iterable):
        """Initializes the CountedIterator with an iterable.

        Args:
            iterable: The iterable to be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Returns the next item in the iterator and increments the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the current count of iterated items."""
        return self.counter
