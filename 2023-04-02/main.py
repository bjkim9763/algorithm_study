import sys

input = sys.stdin.readline

n = int(input()) # 배달 설탕 무게
cnt = 0
while True:
    if n % 5 == 0:
        cnt = cnt + n // 5
        n = 0
    elif n % 5 != 0:
        n -= 3
        cnt += 1
    if n == 0:
        print(cnt)
        break
    elif n < 0:
        print(-1)
        break

