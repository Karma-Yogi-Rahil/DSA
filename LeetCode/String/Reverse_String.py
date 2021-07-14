"""Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

"""s = ["h","e","l","l","o"]


s.reverse()

print(s)
"""
#method 2 
s = ["H","a","n","n","a","h"]
i =0 
j = len(s)

print(s)        
for i in range(len(s)):
    for j in range(len(s)):
            s[i],s[j]=s[j],s[i]
            i+=1
            print(f" from {s} the i is  {s[i]}")
            j-=1
            print(f" from {s} the j is  {s[j]}")


print(s)
