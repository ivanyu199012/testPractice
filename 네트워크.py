#
# [코테 연습] 네트워크 Python :: 위지원의 개발 일기 🐈
# https://weejw.tistory.com/377
#
def solution( n, computers ):
	row_index_2_network_dict = {}

	network_count = 0
	for i in range( len( computers ) ):
		network = None
		if i in row_index_2_network_dict:
			network = row_index_2_network_dict[i]
		else:
			network_count += 1
			network = set([ i ])
			row_index_2_network_dict[ i ] = network
		for j in range( i, len( computers[ i ] ) ):
			if i == j:
				continue

			if computers[ i ][ j ] == 1:
				network.add( j )
				row_index_2_network_dict[ j ] = network
	return network_count

if __name__ == '__main__':
	result = solution( 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]] )
	print(f'solution( 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]] )= { result }, ea = 2, Test = { result ==2 }')
	# result = solution( 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] )
	# print(f'solution( 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] )= { result }, ea = 1, Test = { result ==1 }')
	# result = solution( 4,  [[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
	# print(f'solution( 4,  [[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]] )= { result }, ea = 3, Test = { result ==3 }')
	# result = solution( 9,   [[1, 1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1]])
	# print(f'solution( 9,  [[1, 1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1]] )= { result }, ea = 4, Test = { result ==4 }')
	# result = solution( 1, [[1]])
	# print(f'solution( 1, [[1]] )= { result }, ea = 1, Test = { result == 1 }')
	# result = solution( 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	# print(f'solution( 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]] )= { result }, ea = 3, Test = { result == 3 }')