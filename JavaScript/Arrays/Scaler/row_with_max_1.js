function maxRow(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  let r = 0;
  let c = cols - 1;

  let count = 0;
  let max_row_level = 0;

  while (r < rows && c >= 0) {
    if (matrix[r][c] === 1) {
      max_row_level = r;
      c -= 1;
      count += 1;
    } else {
      r += 1;
    }
  }
  return {
    max_row_level,
    total_ones: count,
  };
}

console.log(
  maxRow([
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
  ])
);
