ncarrots = int(input())
sizes = list(map(int, input().split()))
leftrabbitindex = 0
leftcarrotsize = 0
rightrabbitindex = len(sizes) - 1
rightcarrotsize = 0
eatencarrots = 0
leftrabbitstilleating = True
rightrabbitstilleating = True
eatencarrotsbool = [False] * len(sizes)
while leftrabbitstilleating or rightrabbitstilleating:
    if leftrabbitindex < len(sizes) and sizes[leftrabbitindex] >= leftcarrotsize and leftrabbitstilleating and not eatencarrotsbool[leftrabbitindex]:
        eatencarrots += 1
        eatencarrotsbool[leftrabbitindex] = True
        leftcarrotsize = sizes[leftrabbitindex]
        leftrabbitindex += 1
    else: leftrabbitstilleating = False
    if rightrabbitindex >= 0 and sizes[rightrabbitindex] >= rightcarrotsize and rightrabbitstilleating and not eatencarrotsbool[rightrabbitindex]:
        eatencarrots += 1
        eatencarrotsbool[rightrabbitindex] = True
        rightcarrotsize = sizes[rightrabbitindex]
        rightrabbitindex -= 1
    else: rightrabbitstilleating = False
print(eatencarrots)