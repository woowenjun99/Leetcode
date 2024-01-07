from typing import List
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        l = list(zip(startTime, endTime, profit))
        l.sort()
        for index, value in enumerate(l):
            startTime[index] = value[0]
            endTime[index] = value[1]
            profit[index] = value[2]

        maximum_profit_for_job = profit.copy()
        maximum_after_index = profit.copy()

        for index in range(len(l) - 2, -1, -1):
            first_start_after_end = bisect_left(startTime, endTime[index])
            if first_start_after_end < len(startTime):
                maximum_profit_for_job[index] += maximum_after_index[first_start_after_end]
            maximum_after_index[index] = max(maximum_profit_for_job[index], maximum_after_index[index + 1])

        return max(maximum_profit_for_job)
