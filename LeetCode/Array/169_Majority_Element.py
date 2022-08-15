"""
169. Majority Element - Easy
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""
nums = [3,3,4]

dic = {}

for i in range(0,len(nums)):
    if nums[i] in dic.keys():
        dic[nums[i]] +=1

    else:
        dic[nums[i]] = 1

for key in dic:
    if dic[key] > (len(nums)/2):
        print(key)


