def binary_search(list,target):
    first = 0
    last = len(list)-1
    mid = (first+last)//2

    while first <= last:
        if list[mid] == target:
            return mid

        elif list[mid] < target:
            first = mid +1

        else:
            last = mid - 1

def verify(index):
    if index is not None:
        print("target found at ",index)

    else:
        print("target not found ")


a = [1,2,3,4,5,6,7,8]

result = binary_search(a,7)
verify(result)