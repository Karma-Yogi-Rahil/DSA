
# the link to the problem statement -> https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    d =[]
    # appending name and score to an array(d)
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        d.append([name,score])     
    
 
    #sorting the score list to find secound low score 
    sort_score = sorted(list(set([x[1] for x in d])))
    # index will be the secound low score 
    secound_low = sort_score[1]
    # a list whhich will contain name of students who has secound low score 
    name =[]
    for a,c in d:
        if  c == secound_low :
            name.append(a)
    
    name.sort()
    for a in name:
        print(a)
            
            
        
        
