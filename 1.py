# Two Sum Solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in table:
                return [table[complement], i]

            table[num] = i
