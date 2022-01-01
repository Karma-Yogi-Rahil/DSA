"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. 
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
"""
nums = [1,3,5,6]

target = 7
target1 = [target]
nums = nums +target1
nums.sort()
print(nums)

# method 1 Brute force (Linear search)
for i in range(len(nums)):
    if nums[i] == target:
        print(i)

# Mehtod 2 Binary search 
def binary_search(nums,target):
    lb = 0
    ub = len(nums)-1
    mid =0


    while lb < ub:
        mid = (lb+ub//2)
        if nums[mid] < target:
            lb = mid +1
    
        elif nums[mid] > target:
            ub = mid-1
        else:
            return mid
        

    return -1





    
    




