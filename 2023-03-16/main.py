
N, M = map(int, input("짜장면 개수, 웍의 개수 \n").split())
S = [int(input("후라이팬 용량 : ")) for _ in range(M)]
dp = [10000000000] * (N + 1) # dp[i] = 짜장면 개수가 i일떄 최소 요리 횟수

def cook(total_amount):
    if total_amount < 0:
        return -1
    elif total_amount == 0:
        return 0

    for i in S:
        dp[i] = 1
    dp[2] = dp[1] + dp[1]
    for i in range(3, total_amount + 1):
        dp[i] = min(dp[i], min([dp[j] + dp[k] for j in range(1, i+1) for k in range(1, i - j + 1) if j + k == i]))

    print(dp)
    return dp[total_amount]

ans = cook(N)
print(ans)