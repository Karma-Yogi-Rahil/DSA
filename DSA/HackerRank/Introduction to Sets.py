def average(array):
    total_sum = sum(set(array))
    total_count = len(set(array))
    ans = float(total_sum/total_count)
    return ans 


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)