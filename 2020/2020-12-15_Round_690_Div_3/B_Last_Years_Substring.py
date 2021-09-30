T = int(input())
for tc in range(T):
    n = int(input())
    st = input()
    if st[0:4] == "2020" or st[n - 4:n] == "2020":
        print("YES")
    elif n >= 4 and st[0] == "2" and st[n - 3:n] == "020":
        print("YES")
    elif n >= 4 and st[0:2] == "20" and st[n - 2:n] == "20":
        print("YES")
    elif n >= 4 and st[0:3] == "202" and st[n - 1] == "0":
        print("YES")
    else:
        print("NO")