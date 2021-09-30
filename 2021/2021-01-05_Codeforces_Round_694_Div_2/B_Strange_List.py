T = int(input())
for tc in range(T):
    n, x = map(int, input().split())
    a_array = list(map(int, input().split()))
    i = 0
    summat = 0
    while i < len(a_array):
        if a_array[i] % x != 0:
            break
        a_array += [a_array[i] // x] * x
        i += 1
        # print(a_array)
    print(sum(a_array))

