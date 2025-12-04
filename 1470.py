'''LeetCode question no. 1470 
Q. Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn]'''

class Solution:
    def shuffle(self, nums, n):
        l1 = nums[:n]
        l2 = nums[n:]
        l = []  
        for i in range(n):
            l.append(l1[i])
            l.append(l2[i]) 
        return l
    
#arko method
class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result 