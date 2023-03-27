import sys
# 백준 10986 나머지 합 구하기
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
S = [0] * N # 합배열
C = [0] * M # S의 각 인자를 M으로 나눈 나머지 개수
# S의 인자가 4, M = 3일때 4 % 3 = 1 => C[1] += 1
ans = 0

S[0] = arr[0] #필수
for i in range(1, N):
    S[i] = S[i - 1] + arr[i]
for i in range(N):
    reminder = S[i] % M
    if reminder == 0:
        ans += 1
    C[reminder] += 1
for i in range(M):
    # 예를 들어 C[2] = 2이면 S에 나머지가 2인 인자가 2개이므로 그 차가 0이 될 수 있는 경우가 생김
    # 반면 C[2] < 2 경우에는 같은 수를 뺄 수가 없어 그 차가 0일 수가 없게 된다.
    if C[i] > 1:
        ans += (C[i]*(C[i]-1) // 2)
#
print(ans)