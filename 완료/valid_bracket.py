def solution(s):

	count = 0
	for charactor in s:
		if charactor == "(":
			count += 1
		elif charactor == ")":
			count -= 1

		if count < 0:
			return False

	return count == 0

if __name__ == '__main__':
	print( solution( "()()" ) )
	print( solution( "(())()" ) )
	print( solution( ")()(" ) )
	print( solution( "(()(" ) )


