strings = ['def','de','fgh']
queries = ['de','lmn','fgh']

for i in queries:
    count = 0
    for j in strings:
        if j == queries:
          count +=1

        print(count)

        