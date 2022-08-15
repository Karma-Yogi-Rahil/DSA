"""
Problem Statement
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
 

1. Always num1 should be less than num2

2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied

      a. Sum of the digits of the number is a multiple of 3

      b. Number has only two digits

      c. Number is a multiple of 5

3. Display the maximum element from the list

In case of any invalid data or if the list is empty, display -1.
"""

def find_max(num1, num2):
    max_num=-1
    max_list =[]
 


    if num1 >= num2 :
        return -1


    for i in range(num1-1,num2+1):
        for j in range(i+1)  :
            sum = 0
            sum = sum + int(i)
            if sum%3 == 0:
                if len(str(i))==2 :
                    if i%5==0:
                        max_list.append(i)      

    if len(max_list) == 0:
        return -1 
    else:
        return max_list[-1]

#Provide different values for num1 and num2 and test your program.
max_num=find_max(2,14)
print(max_num)
