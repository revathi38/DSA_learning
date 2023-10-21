def maxRow(matrix):
    rows= len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols-1
    count_one = 0
    
    row = 0

    while i < rows and j >= 0:
        if matrix[i][j] == 1:
            count_one += 1
            row = i
            j -= 1
        else:
            i += 1
    return {
        "max_row_level": row,
        "total_ones": count_one,
        }




print(maxRow([
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1]
]))

# TC: O(rows * cols)
# SC: O(1)

"""
    count_one = 5
    max_row_count = 5
    row = 4
"""