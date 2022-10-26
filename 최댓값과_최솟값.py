#
import heapq


# def solution( s ):

# 	num_str_arr = s.split()
# 	nums = list( map( int, s.split() ) )
# 	neg_nums = [ -1 * num for num in nums ]

# 	heapq.heapify( nums )
# 	heapq.heapify( neg_nums )

# 	min = heapq.heappop( nums )
# 	max = -1 * heapq.heappop( neg_nums )

# 	return str( min ) + ' '  + str( max )

def solution(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))

if __name__ == '__main__':
	print(f'{ solution( "1 2 3 4" )= }, ea = "1 4"')
	print(f'{ solution( "-1 -2 -3 -4" )= }, ea = "-4 -1"')
	print(f'{ solution( "-1 -1" )= }, ea = "-1 -1"')