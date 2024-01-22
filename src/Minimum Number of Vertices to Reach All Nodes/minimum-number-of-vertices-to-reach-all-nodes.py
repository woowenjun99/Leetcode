from typing import List
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges: graph[edge[0]].append(edge[1])

        incoming_edges = [0] * n
        for i in range(n):
            for j in graph[i]: incoming_edges[j] += 1

        result = []
        for i in range(len(incoming_edges)):
            if not incoming_edges[i]: result.append(i)
        
        return result