"""
    Understand
    [1,2,3,3]
    output = 3
    
    [2,1,2,5,3,2]
    output = 2
    
    [5,1,5,2,5,3,5,4]
    output = 5
    
    Plan
    Iterate through all elements and store their counts in a dictionary (elem --> numTimesOccurred). Then iterate through dictionary and output the key that occurs N times.
    """
    
    def repeatedNTimes(self, A: List[int]) -> int:
        counts = {}
        for num in A:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        target = len(A) / 2
        for (num, timesAppeared) in counts.items():
            if timesAppeared == target:
                return num
        return -1