T = int(input())
for tc in range(T):
    n = int(input())
    if len(str(n)) == 1:
        print(n)
    elif n > 45:
        print(-1)
    else:
        minim = -1
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 9]
        i = 7
        while True:
            if digits[i] < i + 1:
                digits[i] += 1
            else:
                i -= 1
                digits[i] += 1
            if sum(digits) == n:
                minim = int(''.join(map(str, digits)))
                break
        print(minim)