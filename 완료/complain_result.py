def solution(id_list, report, k):
	staff_2_target_set_dict = create_staff_2_target_set_dict_by( report )

	id_2_complaint_count_dict = create_id_2_complaint_count_dict_by( id_list, staff_2_target_set_dict )

	complaint_success_id_list = [ id for id in id_2_complaint_count_dict.keys() if id_2_complaint_count_dict[ id ] >= k ]

	answer = get_answer_by(id_list, staff_2_target_set_dict, complaint_success_id_list)
	return answer

def get_answer_by(id_list, staff_2_target_set_dict, complaint_success_id_list ):
	answer = []
	for id in id_list:
		if not id in staff_2_target_set_dict:
			answer.append( 0 )
			continue

		valid_complain_count = 0
		for complaint_success_id in complaint_success_id_list:
			if complaint_success_id in staff_2_target_set_dict[ id ]:
				valid_complain_count += 1
		answer.append( valid_complain_count )
	return answer

def create_staff_2_target_set_dict_by( report ):
	staff_2_target_set_dict = {}
	for complaint_str in report:
		[ staff, target ] = complaint_str.split()
		if not staff in staff_2_target_set_dict:
			staff_2_target_set_dict[ staff ] = set()
		staff_2_target_set_dict[ staff ].add( target )
	return staff_2_target_set_dict

def create_id_2_complaint_count_dict_by( id_list, staff_2_target_set_dict ):
	id_2_complaint_count_dict = {}
	for id in id_list:
		id_2_complaint_count_dict[ id ] = 0
		for target_set in staff_2_target_set_dict.values():
			if id in target_set:
				id_2_complaint_count_dict[ id ] += 1
	return id_2_complaint_count_dict

if __name__ == "__main__":
	print( solution( ["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2 ) )
	print( "------------------" )
	print( solution( ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3 ) )




