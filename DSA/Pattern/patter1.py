"""def hollowSquareDiagonals(rows, ch):
    for i in range(rows):
        for j in range(rows):
            if(i == 0 or i == rows - 1 or j == 0 or j == rows - 1
               or i == j or j == (rows - 1 - i)):
                print('%c ' %ch, end = '')
            else:
                print('  ', end = '')
        print()
    
rows = int(input("Enter Hollow Square Star With Diagonals Rows = "))
ch = input("Symbol to use in Hollow Square With Diagonals = " )

print("Hollow Square With Diagonals Pattern")
hollowSquareDiagonals(rows, ch)"""

"""for i in range(2):
    for j in range (2):
        if i %2 != 0:
            print("*", end='")
        else:
            print(" ",end= " ")

        print(" ")"""
"""row = 3

for i in range(0,row*2):
    for j in range(0,row*2):
        #print(i+j, end='')
        if (i+j) %2==0:
            print("*",end=" ")
        else:
            print(" ",end= " ")
        
        
    print()"""


"""row = 1 
for i in range(0,row*2):
    for j in range(0,row*2):
        #print(i+j, end='')
        if (i+j) %2 !=0:
            print("*",end=" ")
        else:
            print(" ",end= " ")
        
        
    print()"""


"""row = 3
for i in range(0,row*2):
    for j in range(0,row*2):
        print(i+j, end='')
        
        
    print()"""

"""
row = 3
for i in range(0,row*2):
    for j in range(0,row**2):
        #print(i+j, end='')
        if (i==0 or i%2 ==0) and i <=row:
            if j == 0 :
                print("*",end='')

            elif j == row*2 -1:
                print("*",end='')
            
            else:
                print("-",end='')

     

        else:
            if 0<j<row*2-1:
                print("*",end='')
            
            else:
                print("-",end='')



    print()"""

n = 5
c1 = (n*2 - 1) // 2
     
    # For printing lower portion
#c2 =  // 2 - 1

print(c1)
#print(c2)
     
# Loop denoting rows
for i in range(0 , n) :
        # Loop denoting columns
    for j in range(0 , n*2-1) :
             
            # Checking conditions for
            # printing pattern
        
        if (i + j == c1  or j - i == c1 or i == c1 or j ==c1):
                print( "*",end = " ")
        else :
            print(" ",end = " ")    
                
         
    print(" ")   

print("  ")
#c2 = 3 * (n*2-1) / 2 - 1

c2 = n*2 -1 


for i in range (0,n):
    for j in range(n*2-1,0,-1):
        
        #print(i,j," ",end=" ")
        if i+j == c2 or j-i == 1 or i == 0 or j == c1+1:
            print("*",end=" ")
        else:
            print(" ",end=" " )

    print("  ")

print(" ")
c2 = 3 * (n*2-1)// 2 - 1

for i in range (0,n*2-1):
    for j in range(0,n*2-1):
            
        #print(i,j," ",end=" ")
        if i + j == c1  or j - i == c1 or i == c1 or j ==c1 or i+j == c2 or i - j == c1:
            print("*",end=" ")
        else:
            print(" ",end=" " )

    print("  ")

















  
            
        
        
    
  


