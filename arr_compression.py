import math

def solution( s ):

	half_length = math.floor( len( s ) / 2 )
	min_compressed_length = len( s )
	for i in range( 1, half_length + 1 ):
		compressed_str =  get_compressed_str_by( s, i )
		if len( compressed_str ) < min_compressed_length:
			min_compressed_length = len( compressed_str )

	return min_compressed_length

def get_compressed_str_by( text, unit ):
	compressed_str = ""
	index = 0
	j = 0
	while True:

		if index + unit >= len( text ):
			compressed_str += text[ index : index + unit ]
			break

		if text[ index : index + unit ] != text[ index + unit : index + 2*unit ]:
			compressed_str += text[ index : index + unit ]
			index += unit
			continue

		repeated_amount = 1
		for j in range( 2, len( text ) - unit ):
			if text[ index : index + ( j - 1 ) * unit ] != text[ index + unit : index + ( j ) * unit ]:
				break

			repeated_amount = j

		compressed_str += str( repeated_amount ) + text[ index : index + unit ]
		index += ( j - 1 ) * unit

	return compressed_str

if __name__ == '__main__':
	print( solution( "aabbaccc" ) )
	print( solution( "ababcdcdababcdcd" ) )
	print( solution( "abcabcdede" ) )
	print( solution( "abcabcabcabcdededededede" ) )
	print( solution( "xababcdcdababcdcd" ) )

	# print( get_compressed_str_by( "aabbaccc", 1 ) )
	# print( get_compressed_str_by( "aabbaccc", 2 ) )
	# print( get_compressed_str_by( "aabbaccc", 3 ) )
	# print( "--------------------" )

	# print( get_compressed_str_by( "ababcdcdababcdcd", 1 ) )
	# print( get_compressed_str_by( "ababcdcdababcdcd", 2 ) )
	# print( get_compressed_str_by( "ababcdcdababcdcd", 3 ) )
	# print( get_compressed_str_by( "ababcdcdababcdcd", 4 ) )
	# print( get_compressed_str_by( "ababcdcdababcdcd", 5 ) )
	# print( "--------------------" )
