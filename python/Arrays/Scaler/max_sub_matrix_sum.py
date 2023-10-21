def maxSubMatrixSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    pfm_sum = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # prefix sum row wise
    for i in range(rows):
        pfm_sum[i][0] = matrix[i][0]
        for j in range(1, cols):
            pfm_sum[i][j] = pfm_sum[i][j-1] + matrix[i][j]
    
    # prefix sum column wise
    for j in range(cols):        
        for i in range(1, rows):
            pfm_sum[i][j] = pfm_sum[i-1][j] + pfm_sum[i][j]

    max_submatrix_sum = float("-inf")
    for r in range(rows):
        for c in range(cols):
            x1 = r
            y1 = c

            x2 = rows-1
            y2 = cols-1

            curr_sum = pfm_sum[x2][y2]

            if y1 > 0:
                curr_sum -= pfm_sum[x2][y1-1]
            
            if x1 > 0:
                curr_sum -= pfm_sum[x1-1][y2]
            
            if x1 > 0 and y1 > 0:
                curr_sum += pfm_sum[x1-1][y1-1]


            max_submatrix_sum = max(max_submatrix_sum, curr_sum)
    
    
    return max_submatrix_sum


print(maxSubMatrixSum(
    [
        [-5, -4, -3],
        [-1,  2,  3],
        [ 2,  2,  4]        
    ]
))

# TC: O(N^2)
# SC: O(N^2)

"""
pfm_sum  [
            [-5,  -9, -12],
            [-1,   1,  4],
            [ 2,   4,  8],       
        ]


pfm_sum  [
            [-5,  -9, -12],
            [-6,  -8,  -8],
            [-4 , -4,   0],       
        ]

        
    
"""