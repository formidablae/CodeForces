T = int(input())
for tc in range(T):
    n = int(input())
    sequence = list(map(int, input().split()))
    appearen = []
    for i in range(n):
        appearen.append(sequence.count(sequence[i]))

    mimumappear = min(appearen)
    if mimumappear == 1:
        if appearen[0] == 1 or appearen[n - 1] == 1: print(1)
        else:
            if appearen[0] == 2 and appearen[n - 1] == 2:
                print(1)
            else:
                print(2)
    elif appearen[0] == n: print(0)
    else:
        if appearen[0] == mimumappear and appearen[n - 1] == mimumappear:
            print(str(mimumappear - 1))
        elif appearen[0] == mimumappear or appearen[n - 1] == mimumappear:
            print(mimumappear)
        else:
            if appearen[0] == mimumappear + 1 and appearen[n - 1] == mimumappear + 1:
                print(mimumappear)
            else:
                print(str(mimumappear + 1))