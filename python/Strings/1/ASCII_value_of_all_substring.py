"""
Sum of k substring ASCII value
"""


def solve(A, K):
    n = len(A)
    overall = []
    total = 0
    

    for ch in A[:K]:
        total += ord(ch)
    
    l, r = 0, K

    while r < n:
        print(A[r], A[l])
        total += (ord(A[r]) - ord(A[l]))
        overall.append(total)
        l += 1
        r += 1
    
    return overall
    


print(solve("acbadabce", 3))