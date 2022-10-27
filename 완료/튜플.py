#
def solution( s ):
	result = []

	tuples = s[2:-2].split( "},{" )
	tuple_list = []
	for tuple_str in tuples:
		tuple_list.append( [ int( num_str ) for num_str in tuple_str.split( "," )] )

	tuple_list.sort( key=len )

	for i in range( len( tuples ) ):
		li_diff = list( set( tuple_list[ i ] ) - set( result ) )
		result.append( li_diff[ 0 ] )

	return result


if __name__ == '__main__':
	print(f'{ solution( "{{2},{2,1},{2,1,3},{2,1,3,4}}" )= }, ea = [2, 1, 3, 4]')
	print(f'{ solution( "{{1,2,3},{2,1},{1,2,4,3},{2}}" )= }, ea = [2, 1, 3, 4]')
	print(f'{ solution( "{{20,111},{111}}" )= }, ea = [111, 20]')
	print(f'{ solution( "{{123}}" )= }, ea = [123]')
	print(f'{ solution( "{{4,2,3},{3},{2,3,4,1},{2,3}}" )= }, ea = [3, 2, 4, 1]')