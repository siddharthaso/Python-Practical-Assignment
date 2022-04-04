""" Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Constraints:
        - 1 <= n <= 8
    Example 1:
        - Input: n = 3
        - Output: ["((()))","(()())","(())()","()(())","()()()"]
        - Example 2:
    Example 2:
        - Input: n = 1
        - Output: ["()"]  """


"""BRUTE FORCE
import itertools

def valid_string(test):
    check = 0
    for i in test:
        check = (check + 1) if i == "(" else (check -1)
        if check < 0: return False
    return True

def parentheses_combination(n):
    lst = list("()"*n)
    ln = ["".join(i) for i in list(itertools.permutations('()'*n))]
    # print(ln)
    ans = filter(valid_string , ln)

    return sorted(list(set(ans)))

if __name__=='__main__':
    a = int(input("Input : "))
    print("Output: ",parentheses_combination(a)) """




"""Approach 2: Backtracking

Intuition and Algorithm

Instead of adding '(' or ')' every time as in Approach 1, let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.

Complexity Analysis

Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n). This analysis is outside the scope of this article, but it turns out this is the n-th Catalan number 1n+1(2nn)\dfrac{1}{n+1}\binom{2n}{n}n+11​(n2n​), which is bounded asymptotically by 4nnn\dfrac{4^n}{n\sqrt{n}}nn

​4n​.

    Time Complexity : O(4nn)O(\dfrac{4^n}{\sqrt{n}})O(n

​4n​). Each valid sequence has at most n steps during the backtracking procedure.

Space Complexity : O(4nn)O(\dfrac{4^n}{\sqrt{n}})O(n
​4n​), as described above, and using O(n)O(n)O(n) space to store the sequence. """

def parentheses_combination(n):
	ans = []
	def backtrack(S = [], left = 0, right = 0):
		if len(S) == 2 * n:
			ans.append("".join(S))
			return
		if left < n:
			S.append("(")
			backtrack(S, left+1, right)
			S.pop()
		if right < left:
			S.append(")")
			backtrack(S, left, right+1)
			S.pop()
	backtrack()
	return ans

#little better than upper one according to time complexity
def parentheses_combination1(n):
	if n == 0: return ['']
	ans = []
	for c in range(n):
		for left in parentheses_combination(c):
			for right in parentheses_combination(n-1-c):
				ans.append('({}){}'.format(left, right))
	return ans

if __name__=='__main__':
	n = int(input("Input : "))
	print("Output: ",parentheses_combination(n))

""" Closure Number

Intuition

To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.

Consider the closure number of a valid parentheses sequence S: the least index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. Clearly, every parentheses sequence has a unique closure number. We can try to enumerate them individually.

Algorithm

For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1. Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a valid sequence. 
Complexity Analysis

    Time and Space Complexity : O(4nn)O(\dfrac{4^n}{\sqrt{n}})O(n

​4n​). The analysis is similar to Approach 2.

For Approach 3 in Python3, I understand it in this way. Please correct me if I am wrong!
If we enumerate all the possibilities of N = 3. We can get:

[
'((()))', 
'(()())', 
'(())()', 
'()(())', 
'()()()'
]

If we consider the smallest index c of these valid sequences, that can make S[0:2c+1+1] a valid parenthesis sequence. We can see that this closure number c have N posibilities.(If we take duplicated c into account, we can get the Catalan number 5 when n = 3!)

[
'((()))',  # c = 2
'(()())',  # c = 2
'(())()',  # c = 1
'()(())',  # c = 0
'()()()'   # c = 0
]

So we consider all posibilities of c using for c in range(N) loop.

For each c we are subsetting the return sequence(of length: 2N) into 2 part using a pair of parenthesis.
That is why we have '({}){}', the parenthesis in this string represent S[0] and S[2c+1]. The part between them must be valid(the first pair of curly brackets), and the rest of the sequence must be valid(the second pair of curly brackets).

Or in another way, we take the parenthesis in '({}){}' as the root of a binary tree. Then the first pair of curly brackets would be left node and the second pair would be the right node. We are trying to distribute N-1 pairs of parenthesis into a binary tree after we decide our root node.

By using function recursion, we can subset the left part and right part into basic cases, where:

    generateParenthesis(1) would return '()' (Node at the end of branch)
    generateParenthesis(0) would return '' (Leaves)

Hope it might help!
PS: The wikipedia page of Catalan number do help a lot!"""


# # For understanding purpose only
# def parentheses_combination(n):
# 	ans = []
# 	def backtrack(S = [], left = 0, right = 0):
# 		print("-----------------------------------Starting function---------------------------------------")
# 		if len(S) == 2 * n:
# 			ans.append("".join(S))
# 			print("-------------------------------------return----------------------------------------  --ans-- :", ans, "--S-- :", S)
# 			return
# 		if left < n:
# 			S.append("(")
# 			print("left --ans-- :", ans, "--S-- :", S)
# 			backtrack(S, left+1, right)
# 			S.pop()
# 		if right < left:
# 			S.append(")")
# 			print("right --ans-- :", ans, "--S-- :", S)
# 			backtrack(S, left, right+1)
# 			S.pop()
# 			print("-------------------------------------return after poping----------------------------------------")
# 	backtrack()
# 	return ans


# # For understanding purpose only
# def parentheses_combination(n):
# 	if n == 0: return ['']
# 	ans = []

# 	for c in range(n):
# 		print("---------------------------------------------c:", c,"----------------------------------------------")
# 		for left in parentheses_combination(c):
# 			print("-------------------------------------------left :", left,"------------------------------------------------")
# 			for right in parentheses_combination(n-1-c):
# 				print("-------------------------------------------right :", right,"------------------------------------------------")
# 				ans.append('({}){}'.format(left, right))
# 	return ans

# if __name__=='__main__':
# 	n = int(input("Input : "))
# 	print("Output: ",sorted(list(set(parentheses_combination(n)))))
