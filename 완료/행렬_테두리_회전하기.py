def solution(rows, columns, queries):
	answer = []

	num_square = gen_num_square(rows, columns)
	for query in queries:
		answer.append( get_min_n_rotate( num_square, query ) )

	return answer

def gen_num_square( rows, columns ):
	num_square = []
	num = 1
	for _ in range( rows ):
		num_arr = []
		for _ in range( columns ):
			num_arr.append( num )
			num += 1
		num_square.append( num_arr )
	return num_square

def get_min_n_rotate( num_square, query ):

	query = [ num - 1 for num in query ]
	x1, y1, x2, y2 = query
	min_num = num_square[ x1 ][ y1 ]

	coordinate_arr = []
	# top part
	for y in range ( y1, y2 + 1 ):
		coordinate_arr.append( ( x1, y ) )

	# right part
	for x in range ( x1 + 1, x2 ):
		coordinate_arr.append( ( x, y2 ) )

	# bottom part
	for y in range ( y2, y1 - 1, -1 ):
		coordinate_arr.append( ( x2, y ) )
	# print(f'{ coordinate_arr= }')

	# left part
	for x in range ( x2 - 1, x1 , -1 ):
		coordinate_arr.append( ( x, y1 ) )

	ori_coordinate_val = -1
	rotated_coordinate_value = -1
	for i in range ( len( coordinate_arr ) ):
		x, y = coordinate_arr[ i ]

		if ori_coordinate_val == -1:
			rx, ry = coordinate_arr[ i - 1 ]
			rotated_coordinate_value = num_square[ rx ][ ry ]
		else:
			rotated_coordinate_value = ori_coordinate_val
		ori_coordinate_val = num_square[ x ][ y ]
		num_square[ x ][ y ] = rotated_coordinate_value

		min_num = min( min_num, rotated_coordinate_value )

	return min_num




if __name__ == '__main__':
	print(f'{ solution( 6,6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]] ) = }')
	print(f'{ solution( 3,3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]] )= }')
	print(f'{ solution( 100,97, [[1,1,100,97]] )= }')
	# num_square = gen_num_square( 6, 6 )
	# print(f'{ num_square= }')
	# print(f'{ get_min_n_rotate( num_square, [2,2,5,4] )= }')
	# print(f'{ num_square= }')