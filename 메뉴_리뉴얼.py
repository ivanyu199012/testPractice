from collections import Counter
import itertools

def solution(orders, course):
	answer = []
	for course_num in course:
		answer += get_valid_course_by( orders, course_num)
	return sorted( answer )

# def get_valid_course_by( orders, course_num ):
# 	checked_order_arr = []
# 	new_menu_2_count_dict = {}
# 	result_arr = []
# 	for order in orders:
# 		course_combination_arr = get_course_combination( order, course_num )
# 		for course_combination in course_combination_arr:
# 			course_combination_str = "".join( sorted( course_combination ) )
# 			if course_combination_str not in checked_order_arr:
# 				checked_order_arr.append( course_combination_str )
# 			else:
# 				if course_combination_str not in new_menu_2_count_dict:
# 					new_menu_2_count_dict[ course_combination_str ] = 2
# 				else:
# 					new_menu_2_count_dict[ course_combination_str ] += 1

# 	max_count = 2
# 	for new_menu in new_menu_2_count_dict:
# 		if new_menu_2_count_dict[ new_menu ] > max_count:
# 			result_arr = []
# 			result_arr.append( new_menu )
# 			max_count = new_menu_2_count_dict[ new_menu ]
# 		elif new_menu_2_count_dict[ new_menu ] == max_count:
# 			result_arr.append( new_menu )

# 	return result_arr

def get_valid_course_by( orders, course_num ):
	candidates = []
	for order in orders:
		course_combination_arr = list( itertools.combinations( order, course_num ) )
		for course_combination in course_combination_arr:
			candidates.append( "".join( sorted( course_combination ) ) )

	sorted_new_menu_2_count_list = Counter( candidates ).most_common()
	if len( sorted_new_menu_2_count_list ) == 0:
		return []

	max_count = sorted_new_menu_2_count_list[ 0 ][ 1 ]
	if max_count < 2:
		return []

	return [ new_menu for new_menu, count in sorted_new_menu_2_count_list if count == max_count]

if __name__ == '__main__':
	print(f'{ solution( ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4] )= }')
	print(f'{ solution( ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5] )= }')
	print(f'{ solution( ["XYZ", "XWY", "WXA"], [2,3,4] )= }')

	# print(f'{ get_valid_course_by( ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], 2 )= }')
	# print(f'{ get_valid_course_by( ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], 3 )= }')
	# print(f'{ get_valid_course_by( ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], 4 )= }')
	# print(f'{ get_course_combination( "ABCFG", 2 )= }')
	# s = list( "CQWERASFF" )
	# s.sort()
	# s = "".join( s )
	# print(f'{ s= }')