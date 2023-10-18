function rainWaterTrapped(A) {
  const n = A.length;

  // Prefix sum
  const pf_max = new Array(n);
  pf_max[0] = A[0];
  for (let i = 1; i < n; i++) {
    pf_max[i] = A[i] > pf_max[i - 1] ? A[i] : pf_max[i - 1];
  }

  // Suffix sum
  const sf_max = new Array(n);
  sf_max[n - 1] = A[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    sf_max[i] = A[i] > sf_max[i + 1] ? A[i] : sf_max[i + 1];
  }

  let total = 0;
  for (let k = 1; k < n - 1; k++) {
    const l = pf_max[k - 1];
    const r = sf_max[k + 1];
    const level = Math.min(l, r);
    const h = A[k];
    const water = level - h;

    if (water > 0) {
      total += water;
    }
  }

  return total;
}

console.log(rainWaterTrapped([2, 1, 3, 2, 1, 2, 4, 3, 2, 1, 3, 1]));
console.log(rainWaterTrapped([4, 2, 4, 7, 4, 2, 3, 6, 8, 2, 3]));
