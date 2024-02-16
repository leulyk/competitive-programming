# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False

        index = self.hash[val]
        self.data[index] = self.data[-1]
        self.hash[self.data[-1]] = index
        self.data.pop()
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
