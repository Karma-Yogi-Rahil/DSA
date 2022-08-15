"""
204. Count Primes
Easy

3512

843

Add to List

Share
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

"""
"""n = 10
count = 0

if n <= 1:
    print(0)

    
for i in range(2,n):
    if n % i == 0:
        i+=1
        
    else:
        #print(i)
        count +=1
 
    

print(count)"""


x = 10
a=0
if x > 1:
    for n in range(2, x):
        if (x % n) == 0:
            print(x, "is not prime")

        else:
            print(n)
            a +=1


print(a)
        






