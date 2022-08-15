# recursive function 
def factorial(n):
    if n== 0 :
        return 1
    print(n)
    return n*factorial(n-1)
#print(factorial(3))

# Recursion and memory 
def printFunc(n):
    # this is the teminating base case  
    if n == 0 :
        return 0
     
    else:
        print(n)
        # recursive calls to itself again
        return printFunc(n-1)
    
#print(printFunc(4))

# Tower og Hanoi puzzle 

def tower(num_of_disk,start_tower,middle_tower,end_tower):
    if num_of_disk:
        tower(num_of_disk-1,start_tower,middle_tower,end_tower)
        print(num_of_disk-1,start_tower,middle_tower,end_tower)
        print(f"move disk {num_of_disk} from {start_tower} to {end_tower} ")
        tower(num_of_disk-1,middle_tower,end_tower,start_tower)
        print(num_of_disk-1,middle_tower,end_tower,start_tower,"\n")


#tower(3,'a','b','c')

def array(a):
    """if len(a) == 1:
        return  1"""

    return a[0]<= a[1] and array(a[1:])

a = [1,3,5,89]

#print(array(a))

def bit(n):
    if n == 0 :
        return []

    elif n == 1 :
        return ['0','1']
    return [ digit+bitstring for digit in bit(1) for bitstring in bit(n-1) ]

#print(bit(100))

# Path Finding problem  using recue
matrix = [[1,1,1,1,0],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [0,0,0,1,0],
          [1,1,1,1,1]]

def pathFinder(matrix,position,N):
    if position == (N-1,N-1):
        return (N-1,N-1)

    x,y = position
    if x+1 < N and matrix[x+1][y] ==1:
        a = [pathFinder(matrix,(x+1,y),N)]
        if a != None:
            return [(x,y)]+a
    
    if y+1 < N and matrix[x][y+1] == 1:
        (print(matrix[x][y+1]))
        b = [pathFinder(matrix,(x,y+1),N)]
        if b!= None:
            return [(x,y)]+b
    
print(pathFinder(matrix,(0,0),5))