def solve(A):
    n = len(A)
    curr_sum = A[0]
    max_sum = A[0]

    for i in range(len(A)):
        curr_sum = max(curr_sum + A[i], A[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum


print(solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# TC:O(N)
# SC: O(1)
