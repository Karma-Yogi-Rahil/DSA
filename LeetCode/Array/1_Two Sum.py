'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
˳˳˳
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]'''

 # Method 1 (The Brute force way)

Input = [2,7,11,15]
output = []
target = 9

for i in range(len(Input)):
    for j in range(i+1 , len(Input)):
        if Input[i]+Input[j] == target:
            output = [Input[i],Input[j]]
            

print(output)
#Time complexity is O(n^2)

# Method 2 

new_dic ={}
for i in range(len(Input)):
    if (target-Input[i]) in new_dic.keys():
        print(([i, new_dic[target-Input[i]]]))
    else:
        new_dic[Input[i]] = i 
        



       


    




