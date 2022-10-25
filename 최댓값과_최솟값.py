#
import heapq


def solution( s ):

	num_str_arr = s.split()
	nums = [ int( num_str ) for num_str in num_str_arr ]
	neg_nums = [ -1 * num for num in nums ]

	heapq.heapify( nums )
	heapq.heapify( neg_nums )

	min = heapq.heappop( nums )
	max = -1 * heapq.heappop( neg_nums )

	return str( min ) + ' '  + str( max )

if __name__ == '__main__':
	print(f'{ solution( "1 2 3 4" )= }, ea = "1 4"')
	# print(f'{ solution( "-1 -2 -3 -4" )= }, ea = "-4 -1"')
	# print(f'{ solution( "-1 -1" )= }, ea = "-1 -1"')