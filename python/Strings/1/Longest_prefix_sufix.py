"""
Given a string, find the length of longest  prefix substring that is 
also a suffix substring.

"ababcabab"
=> abab
"""

def compute(string):
    n = len(string)

    lps = [0] * n
    l, r = 0, 1

    while r < n:
        if string[l] == string[r]:
            l += 1
            lps[r] = l
            r += 1
        else:
            if l == 0:
                lps[r] = l
                r += 1
            else:
                l = lps[l-1]
    return lps

def longestPrefixSufix(A):
    lps = compute(A)
    length = lps[-1]
    
    if length == 0:
        return ""
    else:
        return A[:length]


print(longestPrefixSufix("ababcabab"))



"""
lps =       0   0   1   2   0   1   2   3   4

            0   1   2   3   4   5   6   7   8
string =    a   b   a   b   c   a   b   a   b

                            l   
                                                r
"""