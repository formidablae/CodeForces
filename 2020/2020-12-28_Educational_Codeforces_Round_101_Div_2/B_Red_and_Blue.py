# import numpy as np
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     reds = list(map(int, input().split()))
#     m = int(input())
#     blues = list(map(int, input().split()))
#     i = 0
#     j = 0
#     maxim = 0
#     summat[0][0] = max(reds[0], blues[0])
#     summat = np.zeros((n, m), dtype=int)
#     while i < n and j < m:
#         if j == 0:
#             summat[i][j] = reds[i]
#         elif i == 0:
#             summat[i][j] = blues[j]
#         else:
#             if reds[i] > blues[j]:
#                 summat[i][j] = summat[i - 1][j] + reds[i]
#                 i += 1
#             else:
#                 summat[i][j] = summat[i][j - 1] + blues[j]
#                 j += 1
#         print(summat)
#     print(summat)
#     print(maxim)