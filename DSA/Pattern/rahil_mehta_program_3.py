n = int(input("Enter pattern length: "))

# Tips of dimaond 
mid = (n*2-1)//2

# Bottom right side of dimond 
right_bottom = 3*mid

# Loop for rows
for i in range (0,n*2-1):
    # Loop for cols
    for j in range(0,n*2-1):
        #print(i,j," ",end=" ")
        #print(i+j, end="  ")
        if i + j == mid  or j - i == mid or i == mid or j ==mid  or i - j == mid or i+j == right_bottom:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print(" ")

