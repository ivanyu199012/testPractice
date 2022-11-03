#
from collections import deque


def solution( rectangle, characterX, characterY, itemX, itemY ):
	count = 0

	not_visited_queue = deque( [ ( characterX, characterY, count )])
	directions = [ [ 0, 1 ], [ 1, 0 ], [ 0, -1 ], [ -1, 0 ]  ]
	visited_set = set()
	while len( not_visited_queue ) > 0:
		x, y, count = not_visited_queue.popleft()

		if ( x, y ) == ( itemX, itemY ):
			return count

		if ( x, y ) in visited_set:
			continue
		visited_set.add( ( x, y ) )

		count += 1
		for dx, dy in directions:
			new_x = x + dx/2
			new_y = y + dy/2

			is_insides_a_rectange = False
			outsides_rectange_count = 0
			for low_x, low_y, high_x, high_y in rectangle:
				if low_x < new_x < high_x and low_y < new_y < high_y:
					is_insides_a_rectange = True
					break
				if new_x < low_x or new_x > high_x or new_y < low_y or new_y > high_y:
					outsides_rectange_count += 1
					continue

			if is_insides_a_rectange:
				continue

			if outsides_rectange_count == len( rectangle ):
				continue

			new_x = new_x + dx/2
			new_y = new_y + dy/2
			if ( new_x, new_y ) not in visited_set:
				not_visited_queue.append( ( new_x , new_y, count ) )

	return count

if __name__ == '__main__':
	result = solution( [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8 )
	print(f'solution( [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8 )= { result }, ea = 17, Test = { result ==17 }')
	result = solution( [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1 )
	print(f'solution( [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1 )= { result }, ea = 11, Test = { result ==11 }')
	result = solution( [[1,1,5,7]], 1, 1, 4, 7 )
	print(f'solution( [[1,1,5,7]], 1, 1, 4, 7 )= { result }, ea = 9, Test = { result ==9 }')
	result = solution( [[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10 )
	print(f'solution( [[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10 )= { result }, ea = 15, Test = { result ==15 }')
	result = solution( [[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3 )
	print(f'solution( [[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3 )= { result }, ea = 10, Test = { result ==10 }')