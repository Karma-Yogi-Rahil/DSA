
"""def generate(numRows: int):
    triangle = [[1]]
        
    for j in range(1, numRows+1):
        prev = triangle[-1]
        triangle.append([1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1])
            
    return triangle

no = int(input())
a = generate(no)
print(sum(a[-1]))"""


b = 'qmExzBIJmdELxyOFWv LOCmefk TwPhargKSPEqSxzveiun'
b = b.upper()
print(b)
a = set(b)
print(a)
print(len(a)-1)