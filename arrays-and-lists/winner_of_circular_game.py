# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))        
        current = 0

        while len(friends) > 1:
            current = (current + k - 1) % len(friends)
            friend = friends.pop(current)
        
        return friends[0]
