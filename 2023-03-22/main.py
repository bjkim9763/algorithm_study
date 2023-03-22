import sys

V, E = map(int, sys.stdin.readline().split())
value = []
arr = []
arr_N = [] #입력 값 개수
arr_even = []
arr_odd = []
for i in range(E):
    value.append(list(map(int, sys.stdin.readline().split())))

for i in value:
    if i not in arr:
        arr.append(i)
a=[]
b=[]
for j in arr:
    if j[0] != j[1]:
        a.append(j[0])
        b.append(j[1])


for i in range(0, V):
    n = a.count(i+1) + b.count(i+1)
    arr_N.append(n)

for i in arr_N:
    if i % 2 == 0 and i != 0:
        arr_even.append(i)
    elif i % 2 != 0:
        arr_odd.append(i)

if (len(arr_odd) == 0 and len(arr_even) != 0) or len(arr_odd) == 2:
    print("YES")
else:
    print("NO")