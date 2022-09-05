def solution( p ):
	return correct_bracket(p)

def correct_bracket(p):

	if len(p) == 0:
		return ""

	if is_valid_bracket_arr( p ):
		return p

	sum = 0
	for i in range( len( p ) ):
		if p[ i ] == "(":
			sum += 1
		elif p[ i ] == ")":
			sum -= 1

		if sum == 0:
			break

	u = p[ :i+1 ]
	v = p[ i+1: ]
	print(f'{ u, v= }')

	if is_valid_bracket_arr( u ):
		return u + correct_bracket( v )
	else:
		result = "(" + correct_bracket( v ) + ")"
		new_u = u[ 1:-1 ]
		for char in new_u:
			if char == "(":
				result += ")"
			else:
				result += "("
		return result


def is_valid_bracket_arr( p ):
	tmp_bracket_arr = []
	for s in p:
		if s == "(":
			tmp_bracket_arr.append( s )
		elif s== ")":
			if len(tmp_bracket_arr) == 0:
				return False
			tmp_bracket_arr.pop()
	return True if len(tmp_bracket_arr) == 0 else False


if __name__ == '__main__':
	print(f'{ solution( "(()())()" )= }')
	print(f'{ solution( ")(" )= }')
	print(f'{ solution( "()))((()" )= }')
	print(f'{ solution( "()))((())(" )= }')
