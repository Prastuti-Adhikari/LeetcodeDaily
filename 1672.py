#richest customer wealth question

class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for account in accounts:
            total_wealth = sum(account)
            if total_wealth > max_wealth:
                max_wealth = total_wealth
        return max_wealth


#also can be done
class Solution:
    def maximumWealth(self, accounts):
        return max([sum(account) for account in accounts])

