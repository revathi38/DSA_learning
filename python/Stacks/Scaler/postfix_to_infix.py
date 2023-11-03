def postfixToInfix(A):
    operators = "+-*/"
    stack = []
    res = 0

    for ch in A:
        if ch not in operators:
            stack.append(ch)
            
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            res = eval((op1) + ch + (op2))
            stack.append(str(res))

    return int(res)


print(postfixToInfix(["2", "1", "+", "3", "*"]))


"""
ch = 3


st = [3

op2 = 1
op1 = 2
res = num(op1) ch num(op2)



"""

"""
1. if ch != operator, push into stack
2. if ch == operator, op2 = pop stack, op1= pop stack, res = eval(op1+ch+op2), push res to stack


"""