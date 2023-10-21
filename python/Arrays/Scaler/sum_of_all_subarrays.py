def sumOfAllSubArrays(A):
    n = len(A)
    total = 0

    for i in range(n):
        count = (i+1) * (n-i)
        total += (count * A[i])

    return total

# TC: O(N)
# SC: O(1)


print(sumOfAllSubArrays([3, 2, 4, 5]))
