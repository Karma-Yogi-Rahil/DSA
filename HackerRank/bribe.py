def minimumBribes(q):
    print(q)
    total_bribes = 0
    swaps = 1
    # If any person is more than 3 places ahead of where they should be,
    # too many bribes have taken place.
    print(q)
    for index, item in enumerate(q):
        if item > index + 3:
            print("Too chaotic")
            return

    # Finally!  
    while (swaps != 0):
        swaps = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                swaps += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                total_bribes += 1
    #print(total_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)