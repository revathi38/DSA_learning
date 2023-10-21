function listSubarraySumZero(A) {
  let total_map = {};
  let total = 0;

  for (let i = 0; i < A.length; i++) {
    total += A[i];

    total_map[total] = i;
  }
}

console.log(listSubarraySumZero([4, 2, -3, -1, 0, 4]));
