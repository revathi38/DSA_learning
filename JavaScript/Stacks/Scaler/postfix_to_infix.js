function postfixToInfix(A) {
  let stack = [];
  const operators = "+-*/";
  let ans;

  for (let ch of A) {
    if (!operators.includes(ch)) {
      stack.push(ch);
    } else {
      let op2 = stack.pop();
      let op1 = stack.pop();
      ans = eval(op2 + ch + op1);
      stack.push(ans.toString());
    }
  }
  return Number(ans);
}

console.log(postfixToInfix(["2", "1", "+", "3", "*"]));
