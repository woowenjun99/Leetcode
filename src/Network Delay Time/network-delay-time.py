from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times: graph[u - 1].append([v - 1, w])
        pq = [[0, k - 1]]
        distances = [float("inf")] * n
        distances[k - 1] = 0
        while pq:
            d, u = heappop(pq)
            if distances[u] > d: continue # Important check
            for v, w in graph[u]:
                if distances[v] <= distances[u] + w: continue
                distances[v] = distances[u] + w
                heappush(pq, [distances[v], v])
        return max(distances) if max(distances) != float("inf") else -1