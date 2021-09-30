import math
import statistics


def distancebetween(a, b):
    dist = 0
    for i in range(len(a)):
        dist += abs(a[i] - b[i])
    return dist


n = int(input())
aarray = list(map(int, input().split()))
mimim = min(aarray)
maxim = max(aarray)
averagevalleft = int(math.floor(statistics.median(aarray)))
previousmindistanceleft = math.inf
mindistanceleft = distancebetween(aarray, [averagevalleft] * n)
averagevalright = int(math.ceil(statistics.median(aarray)))
previousmindistanceright = math.inf
mindistanceright = distancebetween(aarray, [averagevalright] * n)
while previousmindistanceleft >= mindistanceleft and averagevalleft >= mimim:
    averagevalleft -= 1
    previousmindistanceleft, mindistanceleft = mindistanceleft, distancebetween(aarray, [averagevalleft] * n)
while previousmindistanceright >= mindistanceright and averagevalright <= maxim:
    averagevalright += 1
    previousmindistanceright, mindistanceright = mindistanceright, distancebetween(aarray, [averagevalright] * n)
print(min(previousmindistanceleft, mindistanceleft, previousmindistanceright, mindistanceright))