# from functools import reduce
# from math import sqrt
#
#
# def factors(num):
#     step = 2 if num % 2 else 1
#     return set(reduce(list.__add__, ([i, num // i] for i in range(1, int(sqrt(num)) + 1, step) if num % i == 0)))
#
#
# n, m = map(int, input().split())
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))
# answer = []
# for l in range(m):
#     numbers = [b_list[l]] * n
#     for j in range(n):
#         numbers[j] += a_list[j]
#     minim = min(numbers)
#     remanders = 0
#     for k in range(n):
#         remanders += numbers[k] % minim
#     if remanders == 0:
#         answer.append(minim)
#     else:
#         fac = list(factors(minim))
#         fac.sort(reverse=True)
#         i = 1
#         while True:
#             minim = fac[i]
#             remanders = 0
#             for k in range(n):
#                 remanders += numbers[k] % fac[i]
#             if remanders == 0:
#                 answer.append(minim)
#                 break
#             else:
#                 i += 1
# print(*answer)
