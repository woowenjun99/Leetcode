from typing import List

class Solution:
    def execute(self, index, nums: List[int], resp: List[List[int]]):
        if index == len(nums):
            resp.append(nums.copy())
            return
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.execute(index + 1, nums, resp)
            nums[index], nums[i] = nums[i], nums[index]

    def permute(self, nums: List[int]) -> List[List[int]]:
        resp = []
        self.execute(0, nums, resp)
        return resp