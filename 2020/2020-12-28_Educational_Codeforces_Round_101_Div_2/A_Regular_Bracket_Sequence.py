T = int(input())
for tc in range(T):
    seq = list(input())
    # print(seq)
    dim = len(seq)
    if seq[0] == ")" or seq[dim - 1] == "(" or len(seq) % 2 == 1:
        print("NO")
    else:
        indop = seq.index("(")
        indcl = seq.index("(")
        before = indop
        middle = indcl - indop - 1
        after = dim - 1 - indcl
        if (before + after + middle) % 2 == 0:
            print("YES")
        else:
            print("NO")
