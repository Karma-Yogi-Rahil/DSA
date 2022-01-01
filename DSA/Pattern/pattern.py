n = int(input("Enter Pattern Length: "))

#Triangle tip location 
mid = (n*2 - 1) // 2

   
# Loop for  rows
for i in range(0 , n) :
    #Loop for cols    
    for j in range(0 , n*2-1) : 
        #print(i+j,end=" ") 
        # print(i-j,end=" ")  
        if (i + j == mid  or j - i == mid or i == mid or j == mid):
                print("*",end = " ")
        else :
            print(" ",end = " ")   
                
         
    print(" ")   
