# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_histories = {}

        for match in matches: 
            if not player_histories.get(match[0]):
                player_histories[match[0]] = { 'won': 0, 'lost': 0 }
            if not player_histories.get(match[1]):
                player_histories[match[1]] = { 'won': 0, 'lost': 0 }
            player_histories[match[0]]['won'] += 1
            player_histories[match[1]]['lost'] += 1

        winners = [[], []]
        for player_id, player_history in player_histories.items():
            if player_history['lost'] == 0:
                winners[0].append(player_id)
            elif player_history['lost'] == 1:
                winners[1].append(player_id)
        
        winners[0].sort()
        winners[1].sort()

        return winners
