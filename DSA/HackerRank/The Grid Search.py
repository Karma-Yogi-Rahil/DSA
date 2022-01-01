row = int(input())
a=[]
for i in range(row):
    first_input= input().strip()
    a.append(first_input)

pattern_row = int(input())
print(pattern_row)

b = [] 
for i in range(pattern_row):
    patern_input = input().strip()
    b.append(patern_input)

r= 0
pattern_possible = []

for i in range(0,row):
    if r == pattern_row:
        break

    elif b[r] in a[i] and r <= pattern_row:
        print("yes")
        pattern_possible.append(a[i])

        r=r+1
    else:
        print('no')

print(pattern_possible)
    





    
