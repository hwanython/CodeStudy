n = int(input())
A = list(map(int, input().rstrip().split()))
m = int(input())
M = list(map(int, input().rstrip().split()))

print(A,M)



# def binarySearch(array, target, left, right):
#     middle_idx = (left+right)//2
#     print(middle_idx)
#     middle_val = array[middle_idx]
#     if target == middle_val:
#         print("good")
#     elif middle_val > target:
#         binarySearch(array, target, left, middle_idx-1)
#     elif middle_val < target:
#         binarySearch(array, target, middle_idx+1, right)
#     else:
#         return False

# M의 원소가 A에 있다면 =>1 아니면 =>0


A.sort()
targets = M

for target in targets:
    left = 0
    right = len(A) - 1
    error = 0
    correct = 0
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            correct = 1
            print("1")
            break
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if correct == 0:
        print("0")













# for i in M:
#     if i in A:
#         print(1)
#     else:
#         print(0)
