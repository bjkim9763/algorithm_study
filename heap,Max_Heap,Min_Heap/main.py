import heapq

# min_heap 최솟값 차례로 출력
min_heap = []
nums = list(map(int, input().split()))
h = heapq

for num in nums:
    h.heappush(min_heap, num)

while min_heap:
    print(h.heappop(min_heap))

# max_heap 최댓값 차례로 출력
max_heap = []
nums = list(map(int, input().split()))
h = heapq

for num in nums:
    h.heappush(max_heap, (-num,num))

while max_heap:
    print(h.heappop(max_heap)[1])