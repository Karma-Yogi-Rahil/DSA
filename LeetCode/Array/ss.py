x =['ab','cd']

for i in x:
    i.upper()
    print(i)

print(x)
print(bin(29))
 
x =list()
print(x)

print(type(type(x)))

def a():
    try:
        f(x,4)
    except:
        print('after f')

    print('after f ?')

a()


strg = "hello world"
 
k = [(i.upper(),len(i)) for i in strg]
print(k)

print(['qusck', 'teit'][bool('')])


class A:
    def __init__(self):
        self.count = 5
        self.count +=1
a = A()
print(a.count)

list1=[5,3,6,12,13,11,14,0]
print(list1[1:8:2])
print(list1[1:7:2])
print(list1[0:7:2])
print(list1[3:8:2])