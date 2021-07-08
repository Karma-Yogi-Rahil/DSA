"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
#Finding the Answer 
"""A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
Python’s set class represents the mathematical notion of a set. The major advantage of using a set, 
as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. 
This is based on a data structure known as a hash table. 
Since sets are unordered, we cannot access items using indexes like we do in lists. """

# here we are checking the len of the list with the len of the distint list . 
# if the length matches then it will False(list do not contain Duplicate elements) 

nums = [1,2,1,3]

if len(nums) == len(set(nums)):
    print(False)
else:
    print(True)
        