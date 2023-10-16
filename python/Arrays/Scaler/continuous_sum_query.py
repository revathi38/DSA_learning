def solve(A, Q):
    res = [0] * A

    for query in Q:
        L = query[0]
        R = query[1]
        val = query[2]

        res[L-1] += val

        if R < A:
            res[R] -= val
        
    pf = [0] * A
    pf[0] = res[0]

    for i in range(1, A):
        pf[i] = res[i] + pf[i-1]
    
    return pf


    

print(solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]]))