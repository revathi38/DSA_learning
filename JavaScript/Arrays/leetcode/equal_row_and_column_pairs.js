function transposeMatrix(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  const transposed = new Array(cols);
  for (let i = 0; i < cols; i++) {
    transposed[i] = new Array(rows);
    for (let j = 0; j < rows; j++) {
      transposed[i][j] = matrix[j][i];
    }
  }

  return transposed;
}

function equalPairs(matrix) {
  const transpose = transposeMatrix(matrix);

  let rowCount = new Map();
  let count = 0;

  for (let row of matrix) {
    let key = row.toString();
    rowCount.set(key, (rowCount.get(key) || 0) + 1);
  }

  for (let column of transpose) {
    const key = column.toString();
    count += rowCount.get(key) || 0;
  }
  return count;
}

const result = equalPairs([
  [3, 1, 2, 2],
  [1, 4, 4, 5],
  [2, 4, 2, 2],
  [2, 4, 2, 2],
]);
console.log(result);
