import sys

n, m = map(int, sys.stdin.readline().split())
A = [[0]* (n+1)]
D = [[0] * (n+1) for i in range(n+1)]
for i in range(n):
    A_row = [0] + [int(x) for x in sys.stdin.readline().split()]
    A.append(A_row)
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]  #구간 합 구하는 법
        #0행과 0열이 0000으로 구현되어있어서 ㄱㅊ
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(ans)