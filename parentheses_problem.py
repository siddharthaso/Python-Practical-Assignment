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


""" def parentheses_combination(n):
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
	return ans """

#little better than upper one according to time complexity
def parentheses_combination(n):
	if n == 0: return ['']
	ans = []
	for c in range(n):
		print("---------------------------------------------c:", c,"----------------------------------------------")
		for left in parentheses_combination(c):
			print("-------------------------------------------left :", left,"------------------------------------------------")
			for right in parentheses_combination(n-1-c):
				print("-------------------------------------------right :", right,"------------------------------------------------")
				ans.append('({}){}'.format(left, right))
	return ans

if __name__=='__main__':
	n = int(input("Input : "))
	print("Output: ",sorted(list(set(parentheses_combination(n)))))