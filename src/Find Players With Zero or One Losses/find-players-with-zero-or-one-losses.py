from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        matches_played = defaultdict(int)
        
        for winner, loser in matches:
            wins[winner] += 1
            matches_played[winner] += 1
            matches_played[loser] += 1

        appeared = sorted(matches_played.keys())
        response = [[], []]
        for num in appeared:
            if matches_played[num] == wins[num]:
                response[0].append(num)
            elif matches_played[num] == wins[num] + 1:
                response[1].append(num)
        return response