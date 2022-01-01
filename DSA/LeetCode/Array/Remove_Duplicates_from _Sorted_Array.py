"""
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

#the trick here is to start from the last so that your deletions do not change the part of the list you have not yet examined.

a = [0,0,1,1,1,2,2,3,3,4]

         #range(start, stop, step)
for i in range(len(a)-1,0,-1):
    if a[i] == a[i-1]:
        del a[i]
    


print(len(a))
print(a)

