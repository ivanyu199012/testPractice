#
from collections import Counter

def solution( topping ):
	result = 0

	roll_1_count_dict = {}
	roll_1_type_count = 0
	roll_2_count_dict = Counter( topping )
	roll_2_type_count = len( roll_2_count_dict.keys() )

	for topping_item in topping:
		if not topping_item in roll_1_count_dict:
			roll_1_count_dict[ topping_item ] = 1
			roll_1_type_count += 1

		roll_2_count_dict[ topping_item ] = roll_2_count_dict[ topping_item ] - 1
		if roll_2_count_dict[ topping_item ] == 0:
			roll_2_type_count -= 1

		if roll_1_type_count == roll_2_type_count:
			result += 1

	return result

if __name__ == '__main__':
	print(f'{ solution( [1, 2, 1, 3, 1, 4, 1, 2] )= }, ea = 2')
	print(f'{ solution( [1, 2, 3, 1, 4] )= }, ea = 0')