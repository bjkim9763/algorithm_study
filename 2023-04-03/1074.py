import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
visit = 0
while n != 0:
    n -= 1
    half = 2 ** n # 이떄 0 ~ 7 이므로  half는 중앙선 오른쪽에 위치
    if r < half and c < half: # 1사분면
        visit += 0
    elif r < half and c >= half: # 2사분면
        visit += half * half
        c -= half
    elif r >= half and c < half: # 3사분면
        visit += half * half * 2
        r -= half
    else:
        visit += half * half * 3 # 4사분면
        r -= half
        c -= half
print(visit)