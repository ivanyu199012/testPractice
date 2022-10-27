import math


def solution(w,h):


	# square_cut_by_diagonal_count = 0
	# slope = h / w
	# for x in range( w ):
	# 	for y in range( h ):
	# 		if is_cut_by_diagonal( get_2_corners_coor_by( ( x, y ) ), slope ):
	# 			square_cut_by_diagonal_count += 1

	return w * h - ( ( w + h ) - math.gcd( w, h )  )


# slope = h / w
def is_cut_by_diagonal( two_corners_coor_arr, slope ):

	below_diagonal_count = 0
	above_diagonal_count = 0
	for coor in two_corners_coor_arr:
		if coor[ 0 ] * slope > coor[ 1 ]:
			below_diagonal_count += 1
			continue
		if coor[ 0 ] * slope < coor[ 1 ]:
			above_diagonal_count += 1
			continue
	return below_diagonal_count > 0 and above_diagonal_count > 0


def get_2_corners_coor_by( left_down_ep_coor ):
	return [
		( left_down_ep_coor[ 0 ] + 1, left_down_ep_coor[ 1 ] ),
		( left_down_ep_coor[ 0 ], left_down_ep_coor[ 1 ] + 1 ),
	]

if __name__ == '__main__':
	# print( is_cut_by_diagonal( [(0, 0), (1, 0), (0, 1), (1, 1)], 2/3 ) )
	# print( is_cut_by_diagonal( get_4_corners_coor_by( ( 2, 0 ) ), 2/3 ) )
	# print( get_4_corners_coor_by( ( 2, 0 ) ) )
	print( solution( 8, 12 ) )
