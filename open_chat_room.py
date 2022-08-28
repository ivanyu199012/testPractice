
def solution(records):

	uid_2_nickname_dict = get_uid_2_nickname_dict_by(records)
	msg_arr = get_msg_arr_by( uid_2_nickname_dict, records )

	return msg_arr

def get_msg_arr_by( uid_2_nickname_dict, records ):
	msg_arr = []

	for record in records:
		words = record.split()
		uid = words[ 1 ]
		if words[ 0 ] == "Enter":
			msg_arr.append( f"{ uid_2_nickname_dict[ uid ] }님이 들어왔습니다." )
			continue
		if words[ 0 ] == "Leave":
			msg_arr.append( f"{ uid_2_nickname_dict[ uid ] }님이 나갔습니다." )
			continue

	return msg_arr

def get_uid_2_nickname_dict_by(records):
	uid_2_nickname_dict = {}
	for record in records:
		words = record.split()
		if words[ 0 ] in [ "Enter", "Change" ]:
			uid_2_nickname_dict[ words[ 1 ] ] = words[ 2 ]
	return uid_2_nickname_dict

if __name__ == '__main__':
	print( solution( ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"] ) )