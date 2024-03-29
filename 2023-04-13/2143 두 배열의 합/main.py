'''
접근 방법
a와 b의 부배열의 합을 전부 구한뒤 탐색을 통해 조합을 찾는다.


1. 완전 탐색 가능?
import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

asum = [[] for _ in range(n)]
bsum = [[] for _ in range(m)]

for i in range(len(a)):
    sum = a[i]
    asum[i].append(sum)
    for j in range(i+1,len(a)):
        sum += a[j]
        asum[i].append(sum)

for i in range(len(b)):
    sum = b[i]
    bsum[i].append(sum)
    for j in range(i+1,len(b)):
        sum += b[j]
        bsum[i].append(sum)

cnt = 0
for i in asum:
    for j in i:
        for k in bsum:
            if (t - j) in k:
                cnt += 1
print(cnt)

모든 경우를 탐색했지만 시간 초과 발생

2. 이분 탐색으로 시간을 줄여보자
이분 탐색을 하려면 탐색하려는 배열이 오름차순으로 정렬이 되야한다.
따라서 x에 b를 sort시킨다.

** 중요한 개념
bisect는 이분 탐색 함수로 시간 단축에 효율적
예를 들어 2를 찾을 때 bisect_left를 하면 가장 왼쪽에 가까운 2가 몇번째인지 0부터 찾아주고, bisect_right를 하면  가장 오른쪽에 가까운 2가 몇번째인지 1부터 찾아줌
따라서 둘의 차를 구하면 2의 개수를 구할 수 있음 => 중요
'''

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

asum = [[] for _ in range(n)]
bsum = [[] for _ in range(m)]

for i in range(n):
    sum = a[i]
    asum[i].append(sum)
    for j in range(i+1,n):
        sum += a[j]
        asum[i].append(sum)

for i in range(m):
    sum = b[i]
    bsum[i].append(sum)
    for j in range(i+1,m):
        sum += b[j]
        bsum[i].append(sum)

x = []
for i in bsum:
    for j in i:
        x.append(j)

x.sort()
ans = 0
for i in asum:
    for j in i:

        target = t - j # j와 합쳐서 t가 되는 수
        ans += bisect_right(x,target) - bisect_left(x,target) # bisect로 개수 구하기 중요한 개념 이다
print(ans)