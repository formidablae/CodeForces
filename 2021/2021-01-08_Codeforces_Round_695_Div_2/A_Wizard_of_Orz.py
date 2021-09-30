T = int(input())
for tc in range(T):
    n = int(input())
    dig = "989"
    digasc = "0123456789"
    answer = dig[0:min(n, 3)]
    n = n - 3
    if n > 0:
        answer = answer + digasc * (n // 10) + digasc[0: (n % 10)]
    print(answer)

    # n = int(input())
    # dig = "9876543210"
    # answer = dig * (n // 10) + dig[0: (n % 10)]
    # print(answer)