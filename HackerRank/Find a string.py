#ABCDCDC
#CDC  --> 2

def count_substring(string, sub_string):
    for i in string:
        count1 = 0
        if (i+j+k) == sub_string:
            count1 +=1 

        return count1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)