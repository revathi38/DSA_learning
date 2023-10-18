def subarray_sum_zero(A):
    total_map = {}

    total = 0

    for i in range(len(A)):
        total += A[i]

        if(total == 0 or total in total_map):
            start_index = total_map[total] + 1
            return A[start_index: i+1]

        total_map[total] = i


print(subarray_sum_zero([4, 2, -3, 1, 6]))

# TC: O(N)
# SC: O(N)