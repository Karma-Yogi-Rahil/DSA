
n= int(input("Enter pattern length: "))

base = n*2 -1 
# Triangle tip location 
mid = (n*2 - 1) // 2

# Loop for rows 
for i in range (0,n):
    # Loop for cols 
    for j in range(n*2-1,0,-1):
        #print(i,j," ",end=" ")
        #print(j-i,,end=" ")
        if i+j == base or j-i == 1 or i == 0 or j == mid+1:
            print("*",end=" ")
        else:
            print(" ",end=" " )

    print("  ")


