import math

T = int(input())
for tc in range(T):
    n = int(input())
    sequence = list(map(int, input().split()))
    minsteps = math.inf
    for i in range(n):
        select = sequence[i]
        j = 0
        segment = 0
        countsteps = 0
        while len(sequence) > 0 and j < len(sequence):
            if sequence[j] == select:
                if segment == 0: j = j + 1
                else:
                    k = 1
                    while k < segment + 1 and j - segment < len(sequence):
                        sequence.pop(j - segment)
                    countsteps = countsteps + 1
                    segment = 0
                    j = j - k - 1
            else:
                segment = segment + 1
                j = j + 1
        if segment != 0:
            k = 1
            while k < segment + 1 and j - segment < len(sequence):
                sequence.pop(j - segment)
            countsteps = countsteps + 1
            segment = 0
            j = j - k - 1
        minsteps = min(minsteps, countsteps)
    print(minsteps)