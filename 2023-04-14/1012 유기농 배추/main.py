'''
1. 아이디어
matrix에서 1이 서로 인접하는 개수를 찾으면 된다.
처음부터 끝까지 bfs로 탐색한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
ans = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft() # 현재 좌표
        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if chk[ny][nx] == False and arr[ny][nx] == 1:
                    chk[ny][nx] = True
                    q.append((ny, nx))

for i in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    chk = [[False] * m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for j in range(n):
        for l in range(m):
            if chk[j][l] == False and arr[j][l] == 1:
                chk[j][l] = True
                bfs(j, l)
                cnt += 1
    ans.append(cnt)

for i in range(t):
    print(ans[i])

