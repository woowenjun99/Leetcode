from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        incoming_edges = defaultdict(int)
        for t in trust: 
            graph[t[0]].append(t[1])
            incoming_edges[t[1]] += 1
        
        for i in range(1, n + 1):
            if incoming_edges[i] == n - 1 and i not in graph:
                return i

        return -1