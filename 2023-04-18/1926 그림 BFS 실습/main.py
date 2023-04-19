'''
 BFS 너비우선탐색

1. 아이디어
시작점에 연결된 노드 찾기
찾은 노드를 queue에 저장
queue의 가장 먼저 것 뽑아서 반복
1번에 2 5 2번에 3 5번에 4가 있다고 해보자
처음 queue엔 [1, 2, 5]
다음 queue엔 [2, 5, 3]
다음 queue엔 [5, 3, 4]  이런식으로 간다. 그럼 너비 우선 탐색 조건 성립

2. 시간 복잡도
BFS: O(V+E)

3. 자료 구조
검색할 그래프
방문여부 확인(재방문 금지)
Queue: BFS실행
'''
"""
1926 그림

1. 아이디어
- 행과 열로 2중 for문을 돌면서 값이 1인 부분과 방문 여부 X => BFS
- BFS돌면서 그림 개수 +1, 최댓값을 갱신

2. 시간복잡도
- BFS : O(V + E)
- V : 500 * 500
- E : 4 * 500 * 500
- V + E : 5 * 250000 = 125만 < 2억 >> 1초이내 가능

3. 자료구조
- 그래프 전체 지도 : list
- BFS : Queue
- 방문 : list
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n:세로 m:가로
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1] # y축 방향
dx = [1, 0, -1, 0] # x축 방향
# dx, dy는 방향을 의미하므로 0, 1일떄 오른쪽 의미
def bfs(y, x):
    rs = 1 # 크기 의미 처음엔 1
    q = deque()  # () 조심
    q.append((y,x))
    while q:
        ey, ex = q.popleft() # 제일 처음 것
        for k in range(4):
            ny = ey + dy[k] # dy는 세로 방향
            nx = ex + dx[k] # dx는 가로 방향 즉 for문을 돌면서 4방향을 확인하고 ny, nx는 next를 의미
            if 0<= ny<n and 0<=nx<m: # graph의 범위에 포함되 있다면
                if graph[ny][nx] == 1 and visited[ny][nx] == False: # 다음 노드가 1이고, 방문한 적 없다면
                    rs += 1 # 크기 증ㄱ
                    visited[ny][nx] = True # 방문한 적 있음
                    q.append((ny, nx)) # q에 좌표 추가 다음 bfs진행
    return rs

ans = 0
maxv = 0



for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            # bfs를 지나온 점들은 visited가 True이므로 위 조건은 그림인데 방문한 적 없는 걸 의미
            # 전체 그림 개수 += 1
            visited[i][j] = True
            ans += 1
            # BFS > 그림 크기 구해주고
            maxv = max(maxv, bfs(i, j)) # bfs를 통해 얻은 그림 크기와 현재 max중 더 큰걸로 업데이트
            # 최대값 갱신

print(ans)
print(maxv)