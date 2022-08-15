"""
119. Pascal's Triangle II -Easy

Share
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

num = int(input("Enter the number: "))  
list1 = [] #an empty list 
# num +1 for the last list 
num +=1
for i in range(num):   
  list1.append([]) 
  list1[i].append(1)  
  for j in range(1, i):
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j]) 
  if(num != 0):  
    list1[i].append(1) 



print(list1[-1])


