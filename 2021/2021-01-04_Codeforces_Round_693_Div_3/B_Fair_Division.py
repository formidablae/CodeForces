T = int(input())
for tc in range(T):
    n = int(input())
    n_candle_weigths = list(map(int, input().split()))
    tot_sum = sum(n_candle_weigths)
    if tot_sum % 2 == 1:
        print("NO")
    else:
        if (tot_sum // 2) % 2 == 1 and 1 not in n_candle_weigths:
            print("NO")
        else:
            print("YES")
