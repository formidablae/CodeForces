n = int(input())
if n % 2 == 0:
    x = int(n / 2)
    print(int((x + 1) ** 2))
else:
    x = int((n - 1) / 2)
    print(int(((x + 2) ** 2) + x * (x + 2)))