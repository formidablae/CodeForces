T = int(input())

for tc in range(T):
    n = int(input())
    array_a = list(map(int, input().split()))
    even = []
    odds = []
    numbers = []
    for i in range(n):
        if array_a[i] % 2 == 0:
            even.append(array_a[i])
        else:
            odds.append(array_a[i])
    even.sort()
    odds.sort()

    len_even = len(even)
    len_odds = n - len_even
    sum_more_even = 0
    sum_more_odds = 0
    flag_more_even = len_even > len_odds
    flag_more_odds = len_even < len_odds
    if flag_more_even:
        sum_more_even = sum(even[len_even - len_odds - 1:])
    elif flag_more_odds:
        sum_more_odds = sum(odds[len_odds - len_even - 1:])

    score_alice = 0
    score_bob = 0
    while len(even) > 0 or len(odds) > 0:
        if len(even) > 0 and len(odds) > 0:
            if even[-1] - odds[-1] > 0:
                score_alice += even[-1]
                even.pop()
                # bob's turn
                if len(even) > 0:
                    if even[-1] - odds[-1] > 0:
                        even.pop()
                    else:
                        score_bob += odds[-1]
                        odds.pop()
                else:
                    score_bob += odds[-1]
                    odds.pop()
            else:
                odds.pop()
                # bob's turn
                if len(odds) > 0:
                    if even[-1] - odds[-1] > 0:
                        even.pop()
                    else:
                        score_bob += odds[-1]
                        odds.pop()
                else:
                    even.pop()
        elif len(even) > 0:
            # alice's turn
            score_alice += even[-1]
            even.pop()
            # bob's turn
            if len(even) > 0:
                even.pop()
            else:
                break
        elif len(odds) > 0:
            # alice's turn
            odds.pop()
            # bob's turn
            if len(odds) > 0:
                score_bob += odds[-1]
                odds.pop()
            else:
                break
        else:
            break
    if score_alice > score_bob:
        print("Alice")
    elif score_alice < score_bob:
        print("Bob")
    else:
        print("Tie")
