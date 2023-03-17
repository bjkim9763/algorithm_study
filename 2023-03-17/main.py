N, M = map(int, input().split())

dp = [0, 1]
arr = []

for i in range(M):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(2, N + 1):
    cnt = []
    for j in arr:
        if i != j[1]:
            cnt.append(1)
        if i == j[1]:
            cnt.append(dp[j[0]] + 1)

    dp.append(max(cnt))
print(*dp[1:]) # *붙혀주면 대괄호 없이 출력

