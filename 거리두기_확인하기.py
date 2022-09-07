#
def solution( places ):
	result = []
	for i in range(len(places)):
		result.append( is_kept_social_distance( places[i] ) )
	return result

def is_kept_social_distance( place ):

	candidate_coor_list = []
	for i in range( 5 ):
		for j in range( 5 ):
			if place[ i ][ j ] == "P":
				candidate_coor_list.append( ( i, j ) )

	while True:
		if len( candidate_coor_list ) < 2:
			break

		target_x, target_y = candidate_coor_list.pop( 0 )
		for x, y in candidate_coor_list:
			if cal_distance( target_x, target_y, x, y ) == 1:
				return 0

			if cal_distance( target_x, target_y, x, y ) == 2:
				if target_x == x or target_y == y:
					mx, my = ( target_x, ( target_y + y ) / 2 ) if target_x == x else ( ( target_x + x ) / 2, target_y )
					if place[ int( mx ) ][ int( my ) ] != "X":
						return 0
				else:
					if place[ target_x ][ y ] != "X" or place[ x ][ target_y ] != "X":
						return 0
	return 1

def cal_distance( x1, y1, x2, y2 ):
	return abs( x1 - x2 ) + abs( y1 - y2)

if __name__ == '__main__':
	print(f'{ solution( [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]] )= }, ea = [1, 0, 1, 1, 1]')
	# print(f'{ is_kept_social_distance( ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] )= }')