# 2798. Number of Employees Who Met the Target

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if i>=target: count+=1
            continue

        return count