function sumOfAllSubArrays(A) {
  const n = A.length;
  let total = 0;

  for (let i = 0; i < n; i++) {
    const count = (i + 1) * (n - i);
    total += count * A[i];
  }

  return total;
}

console.log(sumOfAllSubArrays([3, 2, 4, 5]));
