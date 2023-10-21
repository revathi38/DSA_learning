"""
Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.



Problem Constraints
1 <= N <=30
0 <= A[i][j] <= 10



Input Format
Single argument representing a 2-D array A of size N x N.



Output Format
Return an integer denoting the sum of all possible submatrices in the given matrix.



Example Input
Input 1:
A = [ [1, 1]
      [1, 1] ]
Input 2:
A = [ [1, 2]
      [3, 4] ]


Example Output
Output 1:
16
Output 2:
40

"""


def AllsubMatrixSum(mat):
    row = len(mat)
    col = len(mat)

    total = 0

    for r in range(row):
        for c in range(col):
            submatrix_counnt = (r+1) * (c+1) * (row - r) * (col - c)
            total += submatrix_counnt * mat[r][c]

    return total


print(AllsubMatrixSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(AllsubMatrixSum([
    [1, 2],
    [3, 4]
]))

# TC: O(N^2)
# SC: O(1)
