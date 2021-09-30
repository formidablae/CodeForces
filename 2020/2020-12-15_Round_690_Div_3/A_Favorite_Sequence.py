T = int(input())
for tc in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    ans = []
    for i in range(n // 2):
        ans.append(seq[i])
        ans.append(seq[n - i - 1])
    if len(seq) % 2 != 0:
        ans.append(seq[len(seq) // 2])
    print(*ans)