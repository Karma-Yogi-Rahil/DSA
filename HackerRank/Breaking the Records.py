scores = [10,5,20,20,4,5,2,25,1]
low_count = 0 
high_count = 0 
high = scores[0]
low = scores[0]

"""for i in range(1,len(scores)):
    print(scores[i])
    if high< scores[i]:
        high = scores[i]
        high_count+=1

    if low > scores[i]:
        low = scores[i]
        low_count+=1"""


for i in range(1, len(scores)):
    if low > scores[i]:
        high = scores[i]
        low_count += 1
    elif high < scores[i]:
        high = scores[i]
        high_count += 1


print(high_count,low_count)
    