"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

"""
# in this we make a dictionary add the new element and pop the number which is alread in the dictionary , and at the end remaing key is the single one 


nums = [4,1,2,1,2]

list_table = {}

for i in nums:
    print(i)
    try:
        list_table.pop(i)
        
    except:
        list_table[i]=1


for i,j in list_table.items():
    print(i)




