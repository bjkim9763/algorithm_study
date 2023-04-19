import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
direction = [input().split() for _ in range(l)]
for i in direction:
    i[0] = int(i[0])

def change_direction(time, direction):
    if