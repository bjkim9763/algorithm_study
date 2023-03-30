import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
diff, r = float("inf"), []
if n == 3:
    print(*sorted(arr))
    sys.exit()
# 배열의 개수가 3개면 반복문을 돌릴 필요가 없다.
# 먼저 정렬된 배열에서 한 개를 미리 선택하고 제거한다.
for i in range(n):
    a = arr.pop() # arr의 맨 오른쪽을 가져오고 제거
    # 시간복잡도를 줄이기 위해 투포인터를 이용한 합 진행
    x, y = 0, len(arr)-1 # 남은 배열중 처음과 끝을 지정

    while(x != y): # x=y가 되버리면 중복이 되므로 안됨
        sum1 = a + arr[x] + arr[y]
        if diff > abs(sum1):  # diff는 0과의 차이를 뜻함 즉 sum1과의 절댓값을 가짐.
            diff = abs(sum1) # diff보다 작다는 뜻은 더 작은 합의 절댓값을 구했다는 의미 diff교체
            r = [a, arr[x], arr[y]] # diff보다 작은 합의 절댓값을 구했으므로 배열 교체

        if diff > sum1: # 크기 비교는 완료. 이때 diff > sum1이면 sum1이 음수라는 의미가 된다.
            x += 1 # 정렬된 배열이므로 가장 왼쪽의 x를 +1해주어 더욱 0에 가깝게 만들어준다.
        else:
            y -= 1 # 정렬된 배열이므로 가장 오른쪽의 y를 -1해주어 0에 근접하게 만들어준다.
        if diff == 0:
            break # diff가 0이라는 것은 값을 찾았다는 것이다. 반복문 진행할 필요가 없다.
    if diff == 0:
        break  # diff가 0이라는 것은 값을 찾았다는 것이다. 반복문 진행할 필요가 없다.

print(*sorted(r))