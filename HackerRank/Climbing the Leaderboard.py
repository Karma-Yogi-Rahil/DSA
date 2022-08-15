#list = 120 100 100 50 50 40 40 20 25 10 5

from typing import Literal


list1 = [100,100 ,50, 40, 40 ,20 ,10]
list2 = [5 ,25 ,50, 120]

'''list1 = list1+list2
list1.sort(reverse=True)
print(list1)'''
list1 = list(set(list1))

for index,i in enumerate( list2):
    #print(index,i)
    list1.append(i)
    list1.sort(reverse=True)
    del list1[list1.index(i):]
    #a = list1.index(i)+1
    print(len(list1)+1)

    
    

"""ranked = [100,100 ,50, 40, 40 ,20 ,10]
player = [5 ,25 ,50, 120]

scores = sorted(list(set(ranked)), reverse=True)
player_ranks = []
for score in player:
    print(score)
    while scores and score >= scores[-1]:
        print("scores",scores)
        scores.pop()
    player_ranks.append(len(scores) + 1)
    print('player',player_ranks)

print(player_ranks)"""




        

