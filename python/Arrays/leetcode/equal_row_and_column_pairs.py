"""
2352. Equal Row and Column Pairs
(Medium)

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

# from

from collections import defaultdict


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


def equalPairs(matrix):
    transposed_matrix = transpose_matrix(matrix)

    row_counts = defaultdict(int)

    count = 0

    for row in matrix:
        row_counts[tuple(row)] += 1

    for column in transposed_matrix:
        count += row_counts[tuple(column)]

    return count

# def equalPairs(matrix):
#     row_counts = defaultdict(int)

#     count = 0

#     for row in matrix:
#         row_counts[tuple(row)] += 1

#     for column in zip(*matrix):
#         count += row_counts[column]

#     return count


print(equalPairs([
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2]
]))


# TC: O(R)
# SC: O(R)
