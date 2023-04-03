n = int(input())
eggs = []
answer = 0
S, W = 0, 1

for _ in range(n):
    eggs.append(list(map(int, input().split())))

def crashEgg(nowIndex):  # 모든 경우의 수를 따진다.
    global answer

    # 종료 조건
    if nowIndex == n: # 현재 index가 배열 길이를 넘음. 즉 가장 최근 깬 계란이 가장 오른쪽 계란
       breakEggs = 0 # 깨진 계란 수
       for i in range(n):
           if eggs[i][S] <= 0:
               breakEggs += 1
       answer = max(answer, breakEggs)  # 재귀함수를 통해 반복, answer는 이전 breakEggs 새로운 breakEggs와 비교 최댓값 뽑기
       return


    if eggs[nowIndex][S] <= 0: # 현재 계란이 이미 깨진 경우
        crashEgg(nowIndex+1)
        return

    # 자기 빼고 다깨진 경우
    isAllEggsCrashed = True
    for i in range(n):
        if i == nowIndex:
            continue
        if eggs[i][S] > 0:
            isAllEggsCrashed = False
            break
    if isAllEggsCrashed:
        answer = max(answer, n - 1)  #이전에 구한 answer값과 자신을 제외한 모든 계란이 다 부서진 경우를 비교. 이떄 이전 answer값이 n, 즉 모든 계란이 부서진 것이 아닌 이상 n-1이 됨
        return

    # 부셔보기

    for targetIndex in range(n):
        if targetIndex == nowIndex: continue
        if eggs[targetIndex][S] <= 0: continue
        # 때리기
        eggs[nowIndex][S] -= eggs[targetIndex][W]
        eggs[targetIndex][S] -= eggs[nowIndex][W]
        crashEgg(nowIndex + 1)
        # 복구
        eggs[nowIndex][S] += eggs[targetIndex][W]
        eggs[targetIndex][S] += eggs[nowIndex][W]


crashEgg(0)
print(answer)