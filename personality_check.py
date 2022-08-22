def solution(survey, choices):

	type_2_score_dict = {
		'R':0,
		'T':0,
		'C':0,
		'F':0,
		'J':0,
		'M':0,
		'A':0,
		'N':0
	}

	cal_score(type_2_score_dict, survey, choices)
	print(f'{ type_2_score_dict= }')

	answer = ''
	return answer

def cal_score(type_2_score_dict, survey, choices):
	arr_len = len( survey )
	for i in range( arr_len ):
		type_pair = survey[ i ]
		choice = choices[ i ]

		if choice >= 4:
			type_2_score_dict[ type_pair[ 1 ] ] += ( choice - 4 )
			continue
		type_2_score_dict[ type_pair[ 0 ] ] += ( 4 - choice )


if __name__ == '__main__':
	solution( ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5] )