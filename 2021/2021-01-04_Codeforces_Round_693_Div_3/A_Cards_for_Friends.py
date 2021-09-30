T = int(input())
for tc in range(T):
    w, h, n_friends = map(int, input().split())
    count = 1
    while w % 2 == 0 or h % 2 == 0:
        if w % 2 == 0:
            w //= 2
            count *= 2
        elif h % 2 == 0:
            h //= 2
            count *= 2
        if count >= n_friends:
            break
    if count >= n_friends:
        print("YES")
    else:
        print("NO")