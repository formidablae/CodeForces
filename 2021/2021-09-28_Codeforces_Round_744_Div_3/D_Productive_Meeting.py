def find_index_of_largest(arr, ind):
    largest_index = -1
    largest = 0
    for indx in range(ind, len(arr)):
        if arr[indx] > largest:
            largest_index = indx
            largest = arr[indx]
    return largest_index


T = int(input())
for tc in range(T):
    N = int(input())
    people_list = list(map(int, input().split()))
    talks = 0
    talks_changed_flag = True
    i = 0
    j = i + 1
    result = ""
    while i < len(people_list) - 1:
        if people_list[i] > 0:
            k = -1
            if talks_changed_flag:
                k = find_index_of_largest(people_list, i + 1)
            if k >= 0:
                if talks > 0:
                    result = result + "\n"
                talks = talks + 1
                result = result + str(i + 1) + " " + str(k + 1)
                people_list[i] = people_list[i] - 1
                people_list[k] = people_list[k] - 1
                talks_changed_flag = True
            elif people_list[j] > 0:
                if talks > 0:
                    result = result + "\n"
                talks = talks + 1
                result = result + str(i + 1) + " " + str(j + 1)
                people_list[i] = people_list[i] - 1
                people_list[j] = people_list[k] - 1
                talks_changed_flag = True
            else:
                j = j + 1
                talks_changed_flag = False
            if j == len(people_list):
                i = i + 1
                j = i + 1
        else:
            i = i + 1
            j = i + 1
            talks_changed_flag = False
    print(talks)
    if talks > 0:
        print(result)
