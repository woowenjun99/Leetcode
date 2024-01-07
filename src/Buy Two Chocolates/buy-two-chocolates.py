from typing import List
from heapq import heappush, heappop

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        pq = []
        for price in prices:
            heappush(pq, -price)
            if len(pq) > 2: heappop(pq)
        return money if -money > sum(pq) else money + sum(pq)