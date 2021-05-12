class Solution:
    """
    Understand
    [[1,2,3],
     [3,2,1]]
    output = 6
    
    []
    output = 0
    
    [[1,2,3]]
    output = 6
    
    [[1,2,3],
     [3,2,2]]
    output = 7
    
    Plan
    For each customer, get the sum of all their bank accounts. Keep track
    of the highest sum found. Return that sum.
    """
    
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            currCustomerWealth = 0
            for bankAccount in customer:
                currCustomerWealth += bankAccount
            if currCustomerWealth > maxWealth:
                maxWealth = currCustomerWealth
        return maxWealth