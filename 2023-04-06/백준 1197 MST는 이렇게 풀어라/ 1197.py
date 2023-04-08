import sys
import heapq

"""
1. 아이디어
- MST 기본문제, 외우기
- 간선을 인접리스트에 집어넣기
- 힙에 시작점 넣기
- 힙이 빌때까지 다음의 작업을 반복
    -힙의 최소값 꺼내서, 해당 노드 방문 안했다면
            - 방문 표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기

2. 시간 복잡도
- MST = O(ElogE)

3. 자료구조
- 간선 저장 되는 인접리스트 : (비용, 노드 번호)
- 힙 : (비용, 노드 번호)
- 방문 여부 : false or True bool[]
- MST 결과값 : int

"""
# MST를 풀 때 heap으로 푼다
# 인접 리스트 이용 => 1번 노드 리스트 = [(w,v)...] 이 때 w는 비용 v는 다음 노드

input = sys.stdin.readline

v, e = map(int, input().split())
edge = [[] for _ in range(v+1)] # 인접 리스트
check = [False] * (v+1)
rs = 0
for i in range(e):
    a, b, c = map(int, input().split())
    edge[a].append([c, b]) # a 와 b를 연결하는 비용 c인 간선
    edge[b].append([c, a])


heap = [[0, 1]]

while heap:
    w, each_node = heapq.heappop(heap) # 최솟값 뽑기
    if check[each_node] == False:
        check[each_node]  = True # 방문 표시
        rs += w
        for next_edge in edge[each_node]:
            if check[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)
print(rs)