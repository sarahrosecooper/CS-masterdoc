class Solution:
    """
    Understand
    [1,2,3,1,1,3]
    output = 4
    
    [1,1,1,1]
    output = 6
    
    [1,2,3]
    output = 0
    
    Plan
    [1,2,3,1,1,3]
    Go through all pairs, and count how many good pairs we have
    """
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numGoodPairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    numGoodPairs += 1
        return numGoodPairs