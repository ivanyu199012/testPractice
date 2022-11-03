#
from collections import deque

def solution( maps ):

	row_amount, col_amount = len( maps ), len( maps[ 0 ])
	not_visited_queue = deque( [ ( 0, 0 ) ] )
	graph = [ [ -1 for _ in range( col_amount ) ] for _ in range( row_amount ) ]
	directions = [ [ 0, 1 ], [ 1, 0 ], [ 0, -1 ], [ -1, 0 ]  ]

	graph[ 0 ][ 0 ] = 1
	while len( not_visited_queue ) > 0:

		x, y = not_visited_queue.popleft()

		for dx, dy in directions:
			new_x = x + dx
			new_y = y + dy

			if  0 <= new_x < row_amount and 0 <=  new_y < col_amount:
				if maps[ new_x ][ new_y ] == 1 and graph[ new_x ][ new_y ] == -1:
					not_visited_queue.append( ( new_x, new_y ) )
					graph[ new_x ][ new_y ] = graph[ x ][ y ] + 1

			if new_x == row_amount - 1 and new_y == col_amount - 1:
				return graph[ new_x ][ new_y ]

	return graph[ -1 ][ -1 ]

if __name__ == '__main__':
	result = solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] )
	print(f'solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] )= { result }, ea = 11, Test = { result ==11 }')
	result = solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] )
	print(f'solution( [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] )= { result }, ea = -1, Test = { result ==-1 }')