function AllsubMatrixSum(matrix) {
  let rows = matrix.length;
  let cols = matrix[0].length;

  let total = 0;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const submatrixCount = (i + 1) * (rows - i) * (j + 1) * (cols - j);
      total += submatrixCount * matrix[i][j];
    }
  }
  return total;
}

console.log(
  AllsubMatrixSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ])
);

console.log(
  AllsubMatrixSum([
    [1, 2],
    [3, 4],
  ])
);
