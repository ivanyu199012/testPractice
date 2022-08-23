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
	answer = get_personality_type_by( type_2_score_dict )
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

def get_personality_type_by( type_2_score_dict ):
	personality_str = ""

	personality_type_tuple_list = [ ( "R", "T" ), ( "C", "F" ), ( "J", "M" ), ( "A", "N" ) ]
	for personality_type_tuple in personality_type_tuple_list:
		if type_2_score_dict[ personality_type_tuple[ 0 ] ] >= type_2_score_dict[ personality_type_tuple[ 1 ] ]:
			personality_str += personality_type_tuple[ 0 ]
		else:
			personality_str += personality_type_tuple[ 1 ]
	return personality_str
