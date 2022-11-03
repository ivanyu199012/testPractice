#
from collections import deque

def solution( maps ):
	count = 0

	not_visited_queue = deque( [ ( 0,0 ) ] )
	visited_set = set( [] )
	row_amount, col_amount = len( maps ),len( maps[ 0 ] )
	directions = [ [ 0, 1 ], [ 1, 0 ], [ 0, -1 ], [ -1, 0 ]  ]
	count = bfs( maps, count, not_visited_queue, visited_set, row_amount, col_amount, directions)
	return count if count < 1E5 else -1

def bfs( maps, count, not_visited_queue : deque, visited_set, row_amount, col_amount, directions):

	if len( not_visited_queue ) == 0:
		return count

	x, y = not_visited_queue.popleft()
	if ( x, y ) in visited_set:
		return 1E5

	count += 1
	if x == row_amount - 1 and y == col_amount - 1:
		return count

	visited_set.add( ( x, y ) )
	possible_directions = []
	for dx, dy in directions:
		new_x = x + dx
		new_y = y + dy

		if new_x < 0 or new_x >= row_amount:
			continue
		elif new_y < 0 or new_y >= col_amount:
			continue
		if maps[ new_x ][ new_y ] == 0:
			continue
		if ( new_x, new_y ) in visited_set:
			continue
		possible_directions.append( [ dx, dy ] )

	if len( possible_directions ) == 0:
			return 1E5

	count_arr = []
	for dx, dy in possible_directions:
		new_x = x + dx
		new_y = y + dy

		if len( possible_directions ) >= 1:
			count = bfs( maps, count, deque( [ ( new_x, new_y ) ] ), visited_set, row_amount, col_amount, directions )
			count_arr.append( count )

	return min( count_arr )


if __name__ == '__main__':
	result = solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] )
	print(f'solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] )= { result }, ea = 11, Test = { result ==11 }')
	result = solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] )
	print(f'solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] )= { result }, ea = -1, Test = { result ==-1 }')