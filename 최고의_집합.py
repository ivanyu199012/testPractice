#
import math


def solution( n, s ):
	answer = []

	if n > s:
		return [-1]

	num = s
	for i in range( n, 0, -1 ):
		element = math.floor( num / i )
		answer.append( element )
		num = num - element

	answer.sort()
	return answer

# def get_multiple( num_arr ):
# 	multiple = 1
# 	for num in num_arr:
# 		multiple *= num
# 	return multiple

if __name__ == '__main__':
	# print(f'{ get_multiple( [4, 5] )= }')
	result = solution( 2, 9 )
	print(f'solution( 2, 9 )= { result }, ea = [4, 5], Test = { result ==[4, 5] }')
	result = solution( 2, 1 )
	print(f'solution( 2, 1 )= { result }, ea = [-1], Test = { result ==[-1] }')
	result = solution( 2, 8 )
	print(f'solution( 2, 8 )= { result }, ea = [4, 4], Test = { result ==[4, 4] }')