'''
1. 문제
트리의 시작점에서 아래로 계속해서 물이 흐른다.
물은 계속해서 자식 노드를 향해 흐르고 리프노드에 다다라서야 멈춘다.
i번 정점에 쌓인 물의 양의 기댓값이 0보다 크다는 것은 물이 있다는 것이고 리프노드를 의미한다.
즉 이 문제에서 전체 물의 양 / 리프노드 합 의 값을 구하면 되는 것이다.
'''

import sys

input = sys.stdin.readline

n, w = map(int, input().split())
leaf_sum = 0
edge = [list(map(int, input().split())) for _ in range(n-1)]
arr = [[] for _ in range(n+1)]
for i in edge:
    arr[i[0]].append(i[1])
    arr[i[1]].append(i[0])
for i in range(2, len(arr)):
    if len(arr[i]) == 1:
        leaf_sum += 1
result = w / leaf_sum
print(arr)
print(result)