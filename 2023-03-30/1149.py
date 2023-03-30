import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n): #처음의 열은 계산하지 않는다.
    arr[i][0] = arr[i][0] + min(arr[i-1][1], arr[i-1][2])
    arr[i][1] = arr[i][1] + min(arr[i-1][0], arr[i-1][2])
    arr[i][2] = arr[i][2] + min(arr[i-1][0], arr[i-1][1])

print(min(arr[n-1]))