# def isHill(lst, ind):
#     return lst[ind - 2] < lst[ind - 1] > lst[ind]
#
#
# def isVall(lst, ind):
#     return lst[ind - 2] > lst[ind - 1] < lst[ind]
#
#
# def numValls(lst):
#     if len(lst) < 3:
#         return 0
#     ind = 2
#     count = 0
#     while ind < len(lst):
#         if isVall(lst, ind):
#             count += 1
#         ind += 1
#     return count
#
#
# def numHills(lst):
#     if len(lst) < 3:
#         return 0
#     ind = 2
#     count = 0
#     while ind < len(lst):
#         if isVall(lst, ind):
#             count += 1
#         ind += 1
#     return count
#
#
# def numHillsAndValls(lst):
#     if len(lst) < 3:
#         return 0
#     ind = 2
#     count = 0
#     while ind < len(lst):
#         if isHill(lst, ind) or isVall(lst, ind):
#             count += 1
#         ind += 1
#     return count
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     n_list = list(map(int, input().split()))
#     if n < 3:
#         print(0)
#     else:
#         count_hills_and_valleys = 0
#         max_reduction = 0
#         now_hill_vall = 0
#         prev_hill_vall = 0
#         prev_prev_hill_vall = 0
#         i = 2
#         while i < n:
#             if isHill(n_list, i) or isVall(n_list, i):
#                 count_hills_and_valleys += 1
#                 now_hill_vall = 1
#             else:
#                 now_hill_vall = 0
#
#             if max_reduction < 3 and prev_prev_hill_vall + prev_hill_vall + now_hill_vall > max_reduction:
#                 if i > 3:
#                     section = n_list[i - 4: i + 1]
#                     count_hills_and_valles = numHillsAndValls(section)
#                     new_min_sec = section.copy()
#                     new_max_sec = section.copy()
#                     new_min_sec[2] = min(section[1], section[3])
#                     new_max_sec[2] = max(section[1], section[3])
#                     # print(new_min_sec)
#                     # print(new_max_sec)
#                     max_reduction = max(max_reduction,
#                                         count_hills_and_valles - min(numHillsAndValls(new_min_sec),
#                                                                      numHillsAndValls(new_max_sec)))
#                 elif i == 3:
#                     section = n_list[i - 3: i + 1]
#                     count_hills_and_valles = numHillsAndValls(section)
#                     new_min_sec = section.copy()
#                     new_max_sec = section.copy()
#                     new_min_sec[1] = min(section[0], section[2])
#                     new_max_sec[1] = max(section[0], section[2])
#                     # print(new_min_sec)
#                     # print(new_max_sec)
#                     max_reduction = max(max_reduction,
#                                         count_hills_and_valles - min(numHillsAndValls(new_min_sec),
#                                                                      numHillsAndValls(new_max_sec)))
#                     new_min_sec = section.copy()
#                     new_max_sec = section.copy()
#                     new_min_sec[2] = min(section[1], section[3])
#                     new_max_sec[2] = max(section[1], section[3])
#                     # print(new_min_sec)
#                     # print(new_max_sec)
#                     max_reduction = max(max_reduction,
#                                         count_hills_and_valles - min(numHillsAndValls(new_min_sec),
#                                                                      numHillsAndValls(new_max_sec)))
#                 else:  # i == 2
#                     section = n_list[i - 2: i + 1]
#                     count_hills_and_valles = numHillsAndValls(section)
#                     new_min_sec = section.copy()
#                     new_max_sec = section.copy()
#                     new_min_sec[1] = min(section[0], section[2])
#                     new_max_sec[1] = max(section[0], section[2])
#                     # print(new_min_sec)
#                     # print(new_max_sec)
#                     max_reduction = max(max_reduction,
#                                         count_hills_and_valles - min(numHillsAndValls(new_min_sec),
#                                                                      numHillsAndValls(new_max_sec)))
#                     # print("new_min_sec", new_min_sec, "numHillsAndValls(new_min_sec):", numHillsAndValls(new_min_sec))
#                     # print("new_max_sec", new_max_sec, "numHillsAndValls(new_max_sec):", numHillsAndValls(new_max_sec))
#                     # print("count_hills_and_valles - min", count_hills_and_valles - min(numHillsAndValls(new_min_sec), numHillsAndValls(new_max_sec)))
#                     # print("count_hills_and_valles", count_hills_and_valles)
#
#             prev_prev_hill_vall = prev_hill_vall
#             prev_hill_vall = now_hill_vall
#             # print("c_hills_valleys:", count_hills_and_valleys, "max_reduction:", max_reduction)
#             i += 1
#         print(count_hills_and_valleys - max_reduction)
