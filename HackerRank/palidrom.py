
a = 'level'
stack = []
poped = ''
for i in a:
    stack.append(i)


while len(stack) != 0 :
    poped = poped + stack.pop()



if poped == a :
    print('its paladrom')

else:
    print('no a palidrome')