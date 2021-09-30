import collections

a, s = list(map(int, input().split()))
diff = s - a
if collections.Counter(list(str(a))) == collections.Counter(list(str(diff))): print("YES")
else: print("NO")