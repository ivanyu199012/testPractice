#
import math

def solution(progresses, speeds):

	remaining_day_list = []
	for i in range( len( progresses ) ):
		remaining_day_list.append( math.ceil( ( 100 - progresses[ i ] ) / speeds[ i ] ) )

	feature_count_arr = []
	first_day = remaining_day_list[ 0 ]
	count = 0
	while True:

		if len( remaining_day_list ) == 0:
			feature_count_arr.append( count )
			return feature_count_arr

		if first_day >= remaining_day_list[ 0 ]:
			remaining_day_list.pop( 0 )
			count += 1
		else:
			feature_count_arr.append( count )
			first_day = remaining_day_list[ 0 ]
			count = 0

if __name__ == '__main__':
	print( solution( [93, 30, 55], [1, 30, 5] ) )
	print( solution( [95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1] ) )
