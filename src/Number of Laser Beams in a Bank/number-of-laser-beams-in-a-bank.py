from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        response = previous = 0

        for row in bank: 
            laser_in_row = row.count("1")
            if not laser_in_row: continue
            response += laser_in_row * previous
            previous = laser_in_row

        return response