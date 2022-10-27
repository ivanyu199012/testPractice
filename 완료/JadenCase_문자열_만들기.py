#
# def solution( s ):
# 	str_arr = s.split( ' ' )

# 	for i in range( len( str_arr ) ):
# 		word = str_arr[ i ]

# 		if len( word ) <= 1:
# 			str_arr[ i ] = word.upper()
# 		else:
# 			str_arr[ i ] = word[ 0 ].upper() + word[ 1: ].lower() if word[ 0 ].isalpha() else word

# 	return ' '.join( str_arr )

def solution( s ):
	str_arr = s.split( ' ' )

	for i in range( len( str_arr ) ):
		str_arr[ i ] = str_arr[ i ].capitalize()

	return ' '.join( str_arr )

if __name__ == '__main__':
	print(f'{ solution( "3people unFollowed me" )= }, ea = "3people Unfollowed Me"')
	print(f'{ solution( "3People unFollowed me" )= }, ea = "3People Unfollowed Me"')
	print(f'{ solution( "3people  unFollowed me" )= }, ea = "3people  Unfollowed Me"')
	print(f'{ solution( "for the last week" )= }, ea = "For The Last Week"')
	print(f'{ solution( "3A" )= }, ea = "3a"')
	print(f'{ solution( " 3A" )= }, ea = " 3A"')
