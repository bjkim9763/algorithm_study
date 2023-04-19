'''
접근 방법]

2가지 조건이 필요하다
1. 간선이 k-1개 이상인 노드를 찾아야 함
=> 그래야 자기 자신을 포함해 k개의 노드가 됨
2. 그 노드들이 서로 친구관계여야 함
=> 서로서로 한명도 빠짐없이

필요한 것들
1. 서로서로가 친구인 점들을 찾자
2. 그 점들이 K개면 출력하고 K개가 아니면 -1 출력

'''

import sys

input = sys.stdin.readline

k, n, f = map(int, input().split())

arr = [[] for _ in range(n+1)]
answer = [-1]
visited = [{i:0 for i in range(1,n+1)} for _ in range(n)]
for i in range(f):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    visited[i][i+1] = 1
    for j in arr[i+1]:
        visited[i][j] = 1
        visited[j-1][i+1] = 1
check = [list(visited[i].values()) for i in range(n)]
for i in range(n):
    if sum(check[i]) >= k-1:
        answer = [i+1]
        for l in range(check[i].count(1)):
            if check[i][l] == 1:
                answer.append(arr[i+1][l])
        break

answer.sort()
for i in range(len(answer)):
    if i > k - 1:
        break
    print(answer[i])

