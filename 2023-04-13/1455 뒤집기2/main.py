'''
접근 방법
먼저 n, m에 따라 행렬을 만들어준다.
** 문자열에 list취하면 분리됨

문제를 보면 (i, j)칸을 뒤집으면 그 이전의 모든 칸도 뒤집어야한다.
이 때 왼쪽부터, 위에 부터 뒤집으면 계속 손해를 보므로 오른쪽부터 아래부터 뒤집는다.
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
cnt = 0

def reverse(i, j):
    for m in range(i + 1):
        for n in range(j + 1):
            if arr[m][n] == 1:
                arr[m][n] = 0
            else:
                arr[m][n] = 1

for i in range(n-1,-1,-1): # n-1부터 0까지 1씩 줄인다.
    for j in range(m-1, -1, -1):  # 거꾸로 세야됨
        if arr[i][j]:
            reverse(i,j)

            cnt += 1


print(cnt)