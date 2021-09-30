t = int(input())
for tc in range(t):
    s = int(input())
    if s % 4 == 1: print("Bob")
    elif s % 4 == 2: print("Alice")
    elif s % 4 == 3: print("Bob")
    else: print("Draw")