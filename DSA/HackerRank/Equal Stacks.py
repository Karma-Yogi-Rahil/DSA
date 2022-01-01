h1 = [1, 1, 1, 1, 2]
h2 = [3, 7]
h3 = [1 ,3, 1]
h1.reverse()
h2.reverse()
h3.reverse()
c1 = []
c2=[]
c3 = []
j=0
k=0 
l = 0 
for i in range(0,len(h1)):
    j+=h1[i]
    c1.append(j)
    
        
    if i < len(h3):
        l+=h3[i]
        c3.append(l)
        

    if i < len(h2):
        k+=h2[i]
        c2.append(k)
        

count = 0
max_height = 0 
while len(c1) and len(c2) and len(c3) !=0  :
    if c1[-1] == c2[-1] and c2[-1] == c3[-1]:
        max_height = c1[-1]
        break



    else:
        if c1[-1] > c2[-1] and c3[-1]:
            c1.pop()
        
        if c2[-1] > c1[-1] and c3[-1]:
            c2.pop()
            
        if c3[-1] > c1[-1] and c2[-1]:
            c3.pop()


        

    
            

    
print(max_height)
    
