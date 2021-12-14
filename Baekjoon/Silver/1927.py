import sys, heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    A = int(sys.stdin.readline())
    if A != 0:
        heapq.heappush(heap, A)
    elif len(heap) < 1:
        print(0)
    else:
        print(heap[0])
        heapq.heappop(heap)

