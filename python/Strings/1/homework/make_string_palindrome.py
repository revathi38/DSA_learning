"""
Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.

Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.



Problem Constraints
1 <= N <= 106



Input Format
The only argument given is a string A.



Output Format
Return an integer denoting the minimum characters needed to be inserted in the beginning to make the string a palindrome string.



Example Input
Input 1:

 A = "abc"
Input 2:

 A = "bb"


Example Output
Output 1:

 2
Output 2:

 0


Example Explanation
Explanation 1:

 Insert 'b' at beginning, string becomes: "babc".
 Insert 'c' at beginning, string becomes: "cbabc".
Explanation 2:

 There is no need to insert any character at the beginning as the string is already a palindrome. 
"""

def create_lps(string):
    n = len(string)
    lps = [0] * n
    
    l = 0
    i = 1

    while i < n:
        if string[l] == string[i]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = l
                i += 1
            else:
                l = lps[l-1]
    return lps


def solve(A):
    lps = create_lps(A + "$" + A[::-1])
    return len(A) - lps[-1]

print(solve("abc"))



"""
N = 7-1
lps     0       0       0       0       0       0       1
        0       1       2       3       4       5       6
A       a       b       c       $       c       b       a

                l
                                                                i
"""