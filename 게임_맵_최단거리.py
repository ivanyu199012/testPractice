#
from collections import deque

def solution( maps ):
	count = 0

	row_max, col_max = len( maps ) - 1, len( maps[ 0 ]) - 1
	not_visited_queue_arr = deque( [ deque( [ ( 0, 0, count ) ] ) ] )
	visited_set = set()
	directions = [ [ 0, 1 ], [ 1, 0 ], [ 0, -1 ], [ -1, 0 ]  ]

	while len( not_visited_queue_arr ) > 0:
		not_visited_queue = not_visited_queue_arr.popleft()
		while len( not_visited_queue ) > 0:
			x, y, count = not_visited_queue.popleft()

			if ( x, y ) in visited_set:
				break
			visited_set.add( ( x, y ) )
			count += 1

			if ( x, y ) == ( row_max, col_max ):
				return count

			possible_directions = []
			for dx, dy in directions:
				new_x = x + dx
				new_y = y + dy

				if new_x < 0 or new_x > row_max:
					continue
				elif new_y < 0 or new_y > col_max:
					continue
				if maps[ new_x ][ new_y ] == 0:
					continue
				if ( new_x, new_y ) in visited_set:
					continue
				possible_directions.append( ( dx, dy ) )

			if len( possible_directions ) == 0:
				break

			for dx, dy in possible_directions:
				new_x = x + dx
				new_y = y + dy

				not_visited_queue_arr.append( deque( [ ( new_x, new_y, count ) ] ) )

			break

	return -1


if __name__ == '__main__':
	result = solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] )
	print(f'solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] )= { result }, ea = 11, Test = { result ==11 }')
	result = solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] )
	print(f'solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] )= { result }, ea = -1, Test = { result ==-1 }')