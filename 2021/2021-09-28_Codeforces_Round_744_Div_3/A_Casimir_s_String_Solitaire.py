T = int(input())
for tc in range(T):
    s = input()
    if len(s) == 2 * s.count("B"):
        print("YES")
    else:
        print("NO")