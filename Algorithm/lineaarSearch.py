def linearSearch(list,target):
    """ Returns the index postions of the target or returns none """

    for i in range(len(list)):
        if list[i] == target:
            return i

    
    return None



def verify(index):
    if index is not None:
        print("target found at ",index)

    else:
        print("target not found ")


a = [1,2,45,6,7,8,9]

result = linearSearch(a,9)
verify(result)
