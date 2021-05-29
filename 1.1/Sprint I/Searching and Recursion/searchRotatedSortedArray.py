'''

Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [1,2,3,4,5,6,7] might become [4,5,6,7,1,2,3]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,1,2,3,4,5], target = 1
Output: 2

Example 2:
Input: nums = [6,7,1,2,3,4,5], target = 3
Output: 4

Example 3:
Input: nums = [1], target = 2
Output: -1

Your solution should have better than O(n) time complexity over the number of items in the list. There is an O(log n) solution. There is also an O(1) solution.

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
Numbers from 1 up to the length of the list will be contained in the list.
'''

def csSearchRotatedSortedArray(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        print(nums[start], " - ",nums[mid], " - ", nums[end])
        if nums[mid] == target:
            return mid
        else:
            if target < nums[mid]:
                if target < nums[start]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                if target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
    return -1
