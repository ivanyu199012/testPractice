#
from itertools import permutations

def solution( expression ):
	result = []

	for perm in permutations( "+-*" ):
		number_list, operator_list = get_numbers_n_operators(expression)
		for operator in perm:
			calculate( number_list, operator_list, operator )
		result.append( abs( number_list[ 0 ] ) )
	return sorted( result )[ -1 ]

def calculate( number_list, operator_list, operator ):

	while True:
		try :
			operator_index = operator_list.index( operator )
			new_value = 0
			if operator == "+":
				new_value = number_list[ operator_index ] + number_list[ operator_index + 1 ]
			elif operator == "-":
				new_value = number_list[ operator_index ] - number_list[ operator_index + 1 ]
			elif operator == "*":
				new_value = number_list[ operator_index ] * number_list[ operator_index + 1 ]
			del operator_list[ operator_index ]
			del number_list[ operator_index ]
			number_list[ operator_index ] = new_value
		except ValueError :
			break

	return None

def get_numbers_n_operators(expression):
	number_list = []
	operator_list = []
	prev_operator_index = -1
	for i, char in enumerate( expression ):
		if not char.isdigit():
			number_list.append( int( expression[ prev_operator_index + 1 : i ] ) )
			operator_list.append( char )
			prev_operator_index = i

	number_list.append( int( expression[ prev_operator_index + 1 : ] ) )
	return number_list, operator_list


if __name__ == '__main__':
	print(f'{ solution( "100-200*300-500+20" )= }, ea = 60420')
	print(f'{ solution( "50*6-3*2" )= }, ea = 300')

	# print(f'{ enumerate("abc")= }')
	# for i, char in enumerate("abc"):
	# 	print(f'{ char, i= }')

	# print(f'{ list( permutations( "+-*" ) )= }')
	# number_list = [100, 200, 300, 500, 20]
	# operator_list = ['-', '*', '-', '+']
	# print(f"{ calculate( number_list, operator_list, '+' )= }")
	# print(f'{ number_list, operator_list= }')