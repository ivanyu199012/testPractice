def solution( triangle ):
	print("solution started")

	if len( triangle ) == 1:
		return triangle[ 0 ][ 0 ]

	sum_arr_arr = []
	for layer in range( len( triangle ) ):
		if layer == 0:
			sum_arr_arr.append( [] )
			sum_arr_arr[ 0 ].append( triangle[ 0 ][ 0 ] )
		if layer > 0:
			num_arr = triangle[ layer ]
			new_sum_arr_arr =  [ [] for i in range( len( num_arr ) ) ]
			for i in range( len( num_arr ) ):
				if i == 0:
					new_sum_arr_arr[ 0 ].append( sum_arr_arr[ i ][ 0 ] + num_arr[ i ] )
				elif i == ( len( num_arr ) - 1 ) :
					new_sum_arr_arr[ i ].append( sum_arr_arr[ -1 ][ 0 ] + num_arr[ i ] )
				else:
					max1 = max( sum_arr_arr[ i - 1 ] )
					max2 = max( sum_arr_arr[ i ] )
					new_sum_arr_arr[ i ] = [ max( max1, max2 ) + num_arr[ i ] ]
			sum_arr_arr = new_sum_arr_arr

	max_num = sum_arr_arr[ 0 ][ 0 ]
	for sum_arr in sum_arr_arr:
		max_sum_arr_num = max( sum_arr )
		max_num = max( max_sum_arr_num, max_num )

	return max_num

if __name__ == '__main__':
	result = solution( [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] )
	print(f'solution( [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] )= { result }, ea = 30, Test = { result ==30 }')