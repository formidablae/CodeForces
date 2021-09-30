T = int(input())
for tc in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    elements = set()
    for num in seq:
        if num not in elements:
            elements.add(num)
        else:
            elements.add(num + 1)
    print(len(elements))