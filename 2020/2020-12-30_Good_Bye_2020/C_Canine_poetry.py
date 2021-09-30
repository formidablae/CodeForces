T = int(input())
# words = ["babba", "abaac", "codeforces", "zeroorez", "abcdcba",
#          "bbbbbbb", "abb", "a", "aa", "aba",
#          "abba", "cba", "cbaa", "cbba", "cbbaa",
#          "ccb", "ccba", "ccbb", "ccbba", "ccbaa",
#          "ccbc", "cbbbbbabbbbc", "bbbbac", "bbbbab", "bbbbba",
#          "cbbbbb", "cccccbbbb"]
# for w in words:
for tc in range(T):
    poem = input()
    # poem = w
    if len(poem) == 0 or len(poem) == 1:
        print(0)
    elif len(poem) == 2:
        if poem[0] == poem[1]:
            print(1)
        else:
            print(0)
    else:
        poem = list(poem)
        count = 0
        if poem[0] == poem[1]:
            count += 1
            poem[1] = "#"
        i = 2
        # print(*poem)
        while i < len(poem):
            if poem[i] == poem[i - 2]:
                count += 1
                poem[i] = "@"
            elif poem[i] == poem[i - 1]:
                count += 1
                poem[i] = "%"
            i += 1
            # print(*poem)
        print(count)
