'''
1. 해결법
-접근 방식 : Y인 것들중에 가장 Y가 많은 것들을 뺸다.
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # n = 기타의 개수, m = 곡의 개수

arr = [input().split() for _ in range(n)]
possiblity = [list(i[1]) for i in arr]

for i in range(n):
    for j in range(m):
        list = [0] * m
        if possiblity[i] >
