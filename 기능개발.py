#
import math


def solution(progresses, speeds):
	answer = []

	remaining_day_list = []
	for i in range( len( progresses ) ):
		remaining_day_list.append( math.ceil( ( 100 - progresses[ i ] ) / speeds[ i ] ) )
	print(f'{ remaining_day_list= }')

	feature_count_arr = []
	first_day = remaining_day_list[ 0 ]
	count = 0
	for i in range( len( remaining_day_list ) ):
		if first_day >= remaining_day_list[ i ]:
			count += 1
		else:
			feature_count_arr.append( count )
			first_day = remaining_day_list[ i ]
			count = 1

	feature_count_arr.append( count )
	return feature_count_arr

if __name__ == '__main__':
	print( solution( [93, 30, 55], [1, 30, 5] ) )
	print( solution( [95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1] ) )
