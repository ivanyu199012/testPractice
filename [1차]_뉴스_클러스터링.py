#
from collections import Counter
import math


def solution( str1, str2 ):

	keyword_list_1 = get_keyword_by( str1 )
	keyword_list_2 = get_keyword_by( str2 )

	counter1 = Counter( keyword_list_1 )
	counter2 = Counter( keyword_list_2 )

	# print(f'{ counter1, counter2= }')
	# print(f'{ ( counter1 & counter2 )= }')
	# print(f'{ ( counter1 | counter2 )= }')

	intersection_list = list( ( counter1 & counter2 ).elements() )
	union_list = list( ( counter1 | counter2 ).elements() )

	if len( union_list ) == 0:
		return 65536
	return int( 65536 *  len( intersection_list) / len( union_list ) )

def get_keyword_by( s ):

	keyword_list = []
	char_list = list( s )
	while len( char_list ) > 1:
		first_char = char_list.pop( 0 )
		if first_char.isalpha() and char_list[ 0 ].isalpha():
			keyword_list.append( ( first_char + char_list[ 0 ] ).upper() )

	return keyword_list

if __name__ == '__main__':
	print(f'{ solution( "FRANCE", "french" )= }, ea = 16384')
	print(f'{ solution( "handshake", "shake hands" )= }, ea = 65536')
	print(f'{ solution( "aa1+aa2", "AAAA12" )= }, ea = 43690')
	print(f'{ solution( "E=M*C^2", "e=m*c^2" )= }, ea = 65536')

	# print(f'{ get_keyword_by( "AAAA12" )= }')
	# print(f'{ get_keyword_by( "FRANCE" )= }')