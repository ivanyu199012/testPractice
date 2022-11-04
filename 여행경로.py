#
from collections import deque

def solution(tickets):

	dep_2_des_list_dict = dict()
	for dep, dest in tickets:
		dep_2_des_list_dict[ dep ] = dep_2_des_list_dict.get( dep, [] ) + [ dest ]

	for dep in dep_2_des_list_dict.keys():
		dep_2_des_list_dict[ dep ].sort( reverse = True )

	path_len = len( tickets ) + 1
	path = []
	if dfs( "ICN", path, dep_2_des_list_dict, path_len ):
		answer = path

	return answer

def dfs( departure, path, dep_2_des_list_dict, path_len ):
	path.append( departure )
	if len( path ) == path_len:
		return True

	if not departure in dep_2_des_list_dict:
		path.pop()
		return False

	for _ in range( len( dep_2_des_list_dict[ departure ] ) ):
		dest = dep_2_des_list_dict[ departure ].pop()

		if dfs( dest, path, dep_2_des_list_dict, path_len ):
			return True

		dep_2_des_list_dict[ departure ].insert( 0, dest )

	path.pop()
	return False

if __name__ == '__main__':
	result = solution( [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] )
	print(f'solution( [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] )= { result }, ea = ["ICN", "JFK", "HND", "IAD"], Test = { result ==["ICN", "JFK", "HND", "IAD"] }')
	result = solution( [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] )
	print(f'solution( [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] )= { result }, ea = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"], Test = { result ==["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] }')