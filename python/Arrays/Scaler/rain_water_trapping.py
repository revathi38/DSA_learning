def rainWaterTrapped(A):
    n = len(A)

    # prefix sum
    pf_max = [A[0]] * n
    for i in range(1, n):
        if A[i] > pf_max[i-1]:
            pf_max[i] = A[i]
        else:
            pf_max[i] = pf_max[i-1]

    # suffix sum
    sf_max = [A[n-1]] * n
    for j in range(n-2, -1, -1):
        if A[i] > sf_max[i+1]:
            sf_max[i] = A[i]
        else:
            sf_max[i] = sf_max[i+1]

    total = 0
    for k in range(1, n-1):
        l = pf_max[k-1]
        r = sf_max[k+1]
        level = min(l, r)
        water = level - A[k]

        if water > 0:
            total += water
    return total


print(rainWaterTrapped([1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))