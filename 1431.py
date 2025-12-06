'''Que no. 1431 Kids with greatest number of candies
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.'''

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []

        for i in candies:
            candies = i + extraCandies
            if candies >= max_candies:
                result.append(True)
            else:
                result.append(False)
                
        return result


#practiced the same question asking user's input
candies = list(map(int, input("Enter the number of candies each child has:").split()))
extra_candies = int(input("Enter the number of extra candies"))
result = []
max_candies = max(candies)

for i in candies:
    if i + extra_candies >= max_candies:
        result.append(True)
    else:
        result.append(False)
print(result)