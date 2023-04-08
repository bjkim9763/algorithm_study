import sys
import heapq

# 각 정점을 잇는 간선 중 비용이 최소인 것 끼리만 모으는 원리
input = sys.stdin.readline

n, m, k = map(int,input().split())
arr = [[] for i in range(n+1)] #간선
rs = []
for i in range(1, m+1):
    a, b = map(int, input().split())
    arr[a].append([i, b]) # i는 비용 b는 정점
    arr[b].append([i, a])



for i in range(k):
    result = 0
    chk = [False] * (n + 1)
    heap = [[0, 1]]  # 0번 노드는 없다. 근데 0을 넣어논 이유는 위의 배열이 1부터 시작하기 떄문. 0번 찍고 1부터 시작한다고 생각한다.
    while heap:  # heap이 다 비워질 때까지

        w, each_node = heapq.heappop(heap)

        if chk[each_node] == False:  # 방문 한 적 없다면
            chk[each_node] = True
            result += w  # 비용만큼 결과 올라감
            for next_edge in arr[each_node]:  # 이동할 노드가 방문한 적 없는 경우만이므로 이미 간 곳은 제외
                if chk[next_edge[1]] == False:
                    heapq.heappush(heap, next_edge)

    if chk[1:].count(False) > 0: # 모든 정점을 방문하지않았다면 0을 rs에 추가
        rs.append(0)
    else:
        rs.append(result)
    for _ in arr:
        for j in _:
            if j[0] == i + 1:
                _.remove(j)  # 모든 과정이 끝난 뒤 arr을 돌며 최소 가중치 노드를 제거한다. i + 1은 0부터 시작하는 test케이스 i 에 1을 더해 등차로 커지는 비용을 표현

print(*rs)