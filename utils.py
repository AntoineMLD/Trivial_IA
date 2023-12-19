"""
This module is devoted to host utility classes and functions
- CircularList (used to generate board and players' turn order)
"""

from typing import Any, List


class CircularList:
    """
    Implements a neverending list,
    first element being the latest's next one.
    This class should be useful to:
    - generate the game's board
    - generate the order of players' turn
    """

    def __init__(self, data: List[Any]):
        self.data = data
        self.index = 0  # Current index, only if we need to use next

    def __getitem__(self, key: int):
        if not isinstance(key, int):
            raise TypeError("Index has to be an integer")
        return self.data[key % len(self.data)]
    
    def __repr__(self):
        return f"[{', '.join(repr(elem) for elem in self.data)}]"

    # Consider not using it if populating from a pre-built data
    def add(self, value: Any):
        self.data.append(value)

    # Useless for boarding the game, useful to switch player's turn
    def next(self):
        if not self.data:  # Handle empty list
            raise IndexError("List is empty")
        item = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
