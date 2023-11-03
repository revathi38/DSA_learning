def isBalancedParanthesis(A):
    stack = []
    openingBrackets = "{(["

    for bracket in A:
        if bracket in openingBrackets:
            stack.append(bracket)
        else:
            if bracket == "]":
                if not stack and stack[-1] != "[":
                    return False
                else:
                    stack.pop()

            elif bracket == ")":
                if not stack and stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif bracket == "}":
                if not stack and stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            else:
                return False
            
    if stack:
        return False
    return True
          



print(isBalancedParanthesis("{([])}"))
print(isBalancedParanthesis("[{}a"))


def isBalancedParanthesis2(A):
    stack = []
    bracket_map = {
        "]": "[", 
        "}":"{", 
        ")":"("
    }

    for bracket in A:
        if bracket in bracket_map.values():
            stack.append(bracket)
        else:
            if bracket in bracket_map:
                if not stack and stack[-1] != bracket_map[bracket]:
                    return False
                else:
                    stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True


print(isBalancedParanthesis2("{([])}"))
print(isBalancedParanthesis2("[{}a"))

# T.C : O(N)
# S.C : O(N)

"""
       b               
A=    {   (   [   ]   )   }

    stack =    

    

"""