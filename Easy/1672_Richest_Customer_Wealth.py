# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = sum(accounts[0])
        for i in range(1, len(accounts)):
            if sum(accounts[i]) > maximum:
                maximum = sum(accounts[i])
            continue
        
        return maximum