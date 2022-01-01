"""
118. Pascal's Triangle
Easy

3058

146

Add to List

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""


# Print Pascal's Triangle in Python
 


num = int(input("Enter the number: "))  
list1 = [] #an empty list  
for i in range(num):
  print(f"{i+1} row ")  
  list1.append([]) 
  list1[i].append(1)  
  
  for j in range(1, i):
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
  
  if(num != 0):  
    if i == 0:
      continue
    list1[i].append(1) 

print(list1,'\n')




print(list1)