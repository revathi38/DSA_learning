function solve(A, Q) {
  let res = new Array(A).fill(0);

  for (let query of Q) {
    let L = query[0];
    let R = query[1];
    let val = query[2];

    res[L - 1] = res[L - 1] + val;

    if (R < A) {
      res[R] -= val;
    }
  }

  pf = new Array(res).fill(0);
  pf[0] = res[0];

  for (let i = 1; i < res.length; i++) {
    pf[i] = res[i] + pf[i - 1];
  }
  return pf;
}

console.log(
  solve(5, [
    [1, 2, 10],
    [2, 3, 20],
    [2, 5, 25],
  ])
);
