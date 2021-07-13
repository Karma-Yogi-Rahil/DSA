"""
Move Zeroes

Solution
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

nums = [0,1,0,3,12]

# Mehthod 1 (My method) 
#min_pointer
i=0
#max_pointer
j= len(nums)
        
#loop untill max and min are same 
while (i !=j):
    if (nums[i] == 0):
        a  = nums[i]
        #removing the element 
        nums.pop(i)
        #adding the element to list from back  
        nums.append(a)
        #Decreasing the j by one because new 0 is now at last 
        j-=1
        
    else:
        #increasing i by 1 because non 0 elemnt was found 
        i+=1


#method 2
lst = [0,0,1]
def move_zeros(lst):
  n = len(lst)
  print(n)
  lst[:] = filter(None, lst)
  print(lst)
  lst.extend([0] * (n - len(lst)))
  print(lst)

move_zeros(lst)


#method 3
j = 0
array_len = len(nums)
for num in nums:
    if (num != 0):
        nums[j] = num
        print(nums[j])
        j += 1
        
for i in range(j, array_len):
    print(nums)
    nums[i] = 0



    
    

    



        
 
       

    

