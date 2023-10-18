function subarraySumZero(A) {
  let total_map = {};
  let total = 0;

  for (let i = 0; i < A.length; i++) {
    total += A[i];

    if (total === 0 || total in total_map) {
      startIndex = total_map[total] + 1;
      return A.slice(startIndex, i + 1);
    }

    total_map[total] = i;
  }
}

console.log(subarraySumZero([4, 2, -3, 1, 6]));
