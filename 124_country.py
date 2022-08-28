from math import remainder
import math


def solution( n ):
	trinary_num_str = ''

	num = n
	while True:
		trinary_num_str = str( num % 3 ) + trinary_num_str
		if num < 3:
			break
		num = math.floor( num / 3 )
	print( f'{ trinary_num_str= }' )

	trinary_2_124_list = [ '1', '2', '4' ]
	answer = ''
	for trinary_num in trinary_num_str:
		answer += trinary_2_124_list[ int( trinary_num ) ]

	return int( answer )

if __name__ == '__main__':
	print(f'{ solution( 1 )= }')
	print(f'{ solution( 2 )= }')
	print(f'{ solution( 3 )= }')
	print(f'{ solution( 4 )= }')