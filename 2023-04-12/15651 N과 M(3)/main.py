import sys

'''
1. 해결법
- dfs를 통한 완전 탐색으로 모든 수열을 출력
- 재귀함수를 이욜해 dfs를 구현
- s 리스트에 숫자를 하나씩 집어넣어서 구현
- 예를 들어 처음엔 1 1 1 다음은 1을 제거 후 2 추가 1 1 2 2제거 후 3추가 1 1 3 3제거 후 1제거 후 2 1 추가
 반복
- 이를 위해 s의 길이가 3이 되면 print 후 return 한다.
 '''
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        s.append(i) # 반복문을 돌며 숫자 추가
        dfs() # 재귀함수 호출 m이 2라면 이 중 반복문 같은 느낌이 난다.
        s.pop() # 재귀 함수가 return됐다는 것은 이전 함수에서 s길이가 m이라는 뜻 또는 모든 반복을 종료했다는 뜻이므로 제일 끝부터 제거해준다.

dfs()
