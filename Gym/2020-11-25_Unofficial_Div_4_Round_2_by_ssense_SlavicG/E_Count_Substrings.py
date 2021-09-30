lenghtstr = int(input())
stringinp = input()
t = input()
before = 0
after = 0
count = 0
remaining = 0
for i in range(len(stringinp) - len(t)):
    if stringinp[i: len(t)] == t:
        before = i
        after = len(stringinp) - i - len(t)
        remaining = before + after
        # do remaining factorial for each finding
        # add 2 to the count in the end