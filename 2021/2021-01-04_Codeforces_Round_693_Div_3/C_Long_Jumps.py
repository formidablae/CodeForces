T = int(input())
for tc in range(T):
    n = int(input())
    array_a = list(map(int, input().split()))
    score = {}
    for i in range(n - 1, -1, -1):
        if i + array_a[i] < n:
            score[i + 1] = array_a[i] + score[i + array_a[i] + 1]
        else:
            score[i + 1] = array_a[i]
        # print(score)
    print(max(score.values()))