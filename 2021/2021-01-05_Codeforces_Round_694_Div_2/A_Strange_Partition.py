import math

T = int(input())
for tc in range(T):
    n, x = map(int, input().split())
    a_array = list(map(int, input().split()))
    minimum = math.ceil(sum(a_array) / x)
    maximum = 0
    for el in a_array:
        maximum += math.ceil(el / x)
    print(minimum, maximum)
