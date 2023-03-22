import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
d = [0] * (n+1)
arr = [0]
a = []
for i in range(n):
    arr.append(int(input()))
l = m+k
for i in range(l):
    a.append(list(map(int, input().split())))
for i in a:
    if i[0] == 1:
        arr[i[1]] = i[2]
        for q in range(1, len(arr)):
            d[q] = d[q - 1] + arr[q]
    elif i[0] == 2:
        print(d[i[2]] - d[i[1]-1])



