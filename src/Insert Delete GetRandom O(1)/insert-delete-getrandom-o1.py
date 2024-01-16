"""
Topic: Hashmap + Array

remove: I forgot that removing any element from an array is O(1) because we can swap
it with the last element and call list.pop() which is an O(1) operation.

add: We need to keep track of the index in a hashmap for the delete operation
in the event that we need to swap with the last element. We also need an array
to call for getRandom in O(1).

getRandom: An O(1) operation because reading from an array is O(1).
"""
import sys
from random import randint

input = sys.stdin.readline

class RandomizedSet:
    def __init__(self):
        self.array = []
        self.appeared = {}

    def insert(self, val: int) -> bool:
        if val in self.appeared: return False
        self.array.append(val)
        self.appeared[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.appeared: return False

        if len(self.array) > 1:
            current_index = self.appeared[val]
            print(current_index, len(self.array))
            self.appeared[self.array[-1]] = current_index
            self.array[current_index], self.array[-1] = self.array[-1], self.array[current_index]

        del self.appeared[val]
        self.array.pop()
        return True

    def getRandom(self) -> int:
        return self.array[randint(0, len(list(self.array)) - 1)]
