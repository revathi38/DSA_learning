def maxSubarrayIndex(A):
    n = len(A)

    max_sum = float("-inf")
    curr_sum = float("-inf")

    l = 0
    r = 0

    for i in range(n):
        curr_sum = max(curr_sum+A[i], A[i])
        if A[i] == curr_sum:
            l = i

        if curr_sum > max_sum:
            r = i
        max_sum = max(curr_sum, max_sum)
    
   
    return {
        "max_sum": max_sum,
        "start_index": l,
        "end_index": r,
        "subarray": A[l:r+1]
    }

print(maxSubarrayIndex([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#TC: O(N)
#SC: O(1)