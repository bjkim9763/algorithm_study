import sys

input = sys.stdin.readline
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

annswer = 0
left, right = 0, max(arr) * M
while left <= right:
    mid = (left + right) // 2

    # 해당 시간으로 입국심사를 할 수 있는 사람 수 구하기
    people = 0
    for time in arr:
        people += mid // time
        if people > M:
            break

    if people < M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer, left,right,mid)