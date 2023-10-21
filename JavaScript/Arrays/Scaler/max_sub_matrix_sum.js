function maxSubMatrixSum(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  let pfm_sum = Array.from({ length: rows }, () => Array.from({ length: cols }, () => 0));

  for (let i = 0; i < rows; i++) {
    pfm_sum[i][0] = matrix[i][0];
    for (let j = 1; j < cols; j++) {
      pfm_sum[i][j] = pfm_sum[i][j - 1] + matrix[i][j];
    }
  }

  for (let j = 0; j < cols; j++) {
    for (let i = 1; i < rows; i++) {
      pfm_sum[i][j] = pfm_sum[i - 1][j] + pfm_sum[i][j];
    }
  }

  let max_sub_matrix_sum = Number.NEGATIVE_INFINITY;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const x1 = r,
        y1 = c,
        x2 = rows - 1,
        y2 = cols - 1;

      let currSum = pfm_sum[x2][y2];

      if (y1 > 0) {
        currSum -= pfm_sum[x2][y1 - 1];
      }
      if (x1 > 0) {
        currSum -= pfm_sum[x1 - 1][y2];
      }
      if (x1 > 0 && y1 > 0) {
        currSum += pfm_sum[x1 - 1][y1 - 1];
      }

      max_sub_matrix_sum = Math.max(max_sub_matrix_sum, currSum);
    }
  }

  return max_sub_matrix_sum;
}

console.log(
  maxSubMatrixSum([
    [-5, -4, -3],
    [-1, 2, 3],
    [2, 2, 4],
  ])
);
