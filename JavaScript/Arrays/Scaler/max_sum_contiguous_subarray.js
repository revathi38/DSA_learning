function solve(A) {
  let maxSum = A[0]; // 5
  let currSum = A[0]; // 2

  for (let i = 1; i < A.length; i++) {
    currSum = Math.max(currSum + A[i], A[i]);
    maxSum = Math.max(maxSum, currSum);
  }

  return maxSum;
}

console.log(solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
