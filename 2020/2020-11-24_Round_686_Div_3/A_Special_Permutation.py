T = int(input())
for tc in range(T):
    n = int(input())
    st = ""
    for x in range(2, n + 1):
        st += str(x)
        st += str(" ")
    st += "1"
    print(st)
