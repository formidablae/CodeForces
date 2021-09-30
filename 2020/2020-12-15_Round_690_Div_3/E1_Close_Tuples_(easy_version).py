# # import itertools
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     seq = list(map(int, input().split()))
#     count = 0
#     seq.sort()
#     for i in range(n):
#         for j in range(i + 1, n):
#             if seq[j] - seq[i] > 2:
#                 break
#             for k in range(j + 1, n):
#                 if seq[k] - seq[i] > 2:
#                     break
#                 else:
#                     count += 1
#     # comb = itertools.combinations(seq, 3)
#     # for c in comb:
#     #     print(c)
#     #     if max(c) - min(c) <= 2:
#     #         count += 1
#     print(count)