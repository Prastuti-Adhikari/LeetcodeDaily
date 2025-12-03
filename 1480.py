#Question 1480 Running sum of 1d array
'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        sum_total = 0
    
        for number in nums:
            sum_total += number
            result.append(sum_total)

        return result
    
    #another method
    class Solution:
        def runningSum(self, nums: list[int]) -> list[int]:
            for i in range(1, len(nums)):
                nums[i] += nums[i-1]
            return nums
