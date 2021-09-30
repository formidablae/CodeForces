# from itertools import permutations
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     reds = input()
#     blues = input()
#     morereds = 0
#     # summat_r = 0
#     # summat_b = 0
#     # for i in range(n):
#     #     inner_r_sum = 0
#     #     inner_b_sum = 0
#     #     # morereds += sum(num > blues[n] for num in reds)
#     #     # morereds -= sum(num < blues[n] for num in reds)
#     #     for j in range(n):
#     #         # if reds[i] > blues[j]:
#     #         #     morereds += 1
#     #         # elif reds[i] < blues[j]:
#     #         #     morereds -= 1
#     #         if i == 0 and reds[j] == 0:
#     #             inner_r_sum == inner_r_sum
#     #         else:
#     #             inner_r_sum += reds[j] * (n - 1)
#     #         if i == 0 and blues[j] == 0:
#     #             inner_b_sum == inner_b_sum
#     #         else:
#     #             inner_b_sum += blues[j] * (n - 1)
#     #     summat_r += inner_r_sum * 10 ** (n - i - 1)
#     #     summat_b += inner_b_sum * 10 ** (n - i - 1)
#     # # if morereds > 0:
#     # #     print("RED")
#     # # elif morereds < 0:
#     # #     print("BLUE")
#     # # else:
#     # #     print("EQUAL")
#     # if summat_r > summat_b:
#     #     print("RED")
#     # elif summat_r < summat_b:
#     #     print("BLUE")
#     # else:
#     #     print("EQUAL")
#     perm_r = list(permutations(reds))
#     perm_b = list(permutations(blues))
#     for i in range(len(perm_r)):
#         if perm_r[i] > perm_b[i]:
#             morereds += 1
#         elif perm_r[i] < perm_b[i]:
#             morereds -= 1
#     if morereds > 0:
#         print("RED")
#     elif morereds < 0:
#         print("BLUE")
#     else:
#         print("EQUAL")