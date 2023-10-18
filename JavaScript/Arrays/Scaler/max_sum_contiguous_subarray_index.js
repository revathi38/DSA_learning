function maxSubArrayIndex(A) {
  let currSum = Number.NEGATIVE_INFINITY;
  let maxSum = Number.NEGATIVE_INFINITY;

  let l = 0;
  let r = 0;

  for (let i = 0; i < A.length; i++) {
    currSum = Math.max(currSum + A[i], A[i]);
    if (A[i] === currSum) {
      l = i;
    }

    if (currSum > maxSum) {
      r = i;
    }
    maxSum = Math.max(maxSum, currSum);
  }
  return {
    max_sum: maxSum,
    start_index: l,
    end_index: r,
    subarray: A.slice(l, r + 1),
  };
}
console.log(maxSubArrayIndex([-2, 1, -3, 4, -1, 2, 1, -5, 4]));

//TC: O(N)
//SC: O(1)
