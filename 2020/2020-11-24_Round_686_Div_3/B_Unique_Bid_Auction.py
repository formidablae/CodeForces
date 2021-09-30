import math

T = int(input())
for tc in range(T):
    n = int(input())
    chosennumbers = list(map(int, input().split()))
    mimim = math.inf
    flag = True
    if len(chosennumbers) == 1:
        print("1")
    elif len(chosennumbers) == 2:
        if chosennumbers[0] == chosennumbers[1]: print("-1")
        elif chosennumbers[0] < chosennumbers[1]: print("1")
        else: print("2")
    else:
        chosennumberssorted = chosennumbers.copy()
        chosennumberssorted.sort()
        while len(chosennumberssorted) > 1:
            if chosennumberssorted[0] == chosennumberssorted[1]:
                flag = False
                number = chosennumberssorted[0]
                while len(chosennumberssorted) > 0 and chosennumberssorted[0] == number:
                    chosennumberssorted.pop(0)
            else:
                flag = True
                mimim = chosennumberssorted[0]
                print(str(chosennumbers.index(chosennumberssorted[0]) + 1))
                break
        if not flag and len(chosennumberssorted) == 1:
            print(str(chosennumbers.index(chosennumberssorted[0]) + 1))
        elif not flag:
            print("-1")