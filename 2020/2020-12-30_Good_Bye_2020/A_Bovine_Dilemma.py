T = int(input())
for tc in range(T):
    n = int(input())
    x_coord = list(map(int, input().split()))
    diffs = set()
    for i in range(n):
        for j in range(i + 1, n):
            diffs.add(x_coord[j] - x_coord[i])
    print(len(diffs))