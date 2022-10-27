#
# def solution( triangle ):

# 	sum = 0
# 	sum = cal_tri_sum( triangle, 0, sum, 0 )

# 	return sum

# def cal_tri_sum( triangle, layer, sum, index ):

# 	sum += triangle[ layer ][ index ]

# 	if layer == ( len( triangle ) - 1):
# 		return sum

# 	sum1 = cal_tri_sum( triangle, layer + 1, sum, index )
# 	sum2 = cal_tri_sum( triangle, layer + 1, sum, index + 1 )
# 	return max( sum1, sum2 )


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
	print(f'{ result= }, ea = 30, Result = { result==30 }')