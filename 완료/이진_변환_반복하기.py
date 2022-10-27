#
def solution( s ):

	count = 0
	removed_zero_count = 0
	while s != '1':
		removed_zero_count += len( s.replace( '1', '' ) )
		s_len = len( s.replace( '0', '' ) )
		s = bin( s_len ).replace("0b", "")
		count += 1
		pass

	return [ count, removed_zero_count ]

if __name__ == '__main__':
	print(f'{ solution( "110010101001" )= }, ea = [3,8], Result = { solution( "110010101001" )==[3,8] }')
	print(f'{ solution( "01110" )= }, ea = [3,3], Result = { solution( "01110" )==[3,3] }')
	print(f'{ solution( "1111111" )= }, ea = [4,1], Result = { solution( "1111111" )==[4,1] }')