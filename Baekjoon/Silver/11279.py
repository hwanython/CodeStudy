import sys, heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    A = int(sys.stdin.readline())
    if A != 0:
        heapq.heappush(heap, -1 * A)
    elif len(heap) < 1:
        print(0)
    else:
        print(-1 * heap[0])
        heapq.heappop(heap)

