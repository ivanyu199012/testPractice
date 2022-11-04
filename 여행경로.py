#
from collections import deque

def solution(tickets):
	not_visited_queue = deque( [ ( "ICN", 0, [ False for _ in tickets ], [ "ICN" ] ) ] )
	answer_arr = []
	while len( not_visited_queue ) > 0:
		departure, count, is_used_tickets_arr, path = not_visited_queue.popleft()
		if count == len( tickets ):
			answer_arr.append( path )
			continue

		for i in range( len( tickets ) ):
			if is_used_tickets_arr[ i ]:
				continue

			ticket_departure, ticket_arrival = tickets[ i ]
			if ticket_departure == departure:
				new_is_used_tickets_arr = is_used_tickets_arr.copy()
				new_path = path.copy()
				new_is_used_tickets_arr[ i ] = True
				new_path.append( ticket_arrival )
				not_visited_queue.append( ( ticket_arrival, count + 1, new_is_used_tickets_arr, new_path ) )

	if len( answer_arr ) == 1:
		return answer_arr[ 0 ]

	answer_arr_len = len( answer_arr[ 0 ] )
	for i in range( 1, answer_arr_len ):
		element_arr = [ answer[ i ] for answer in answer_arr ]
		element_arr.sort()
		new_answer_arr = [ answer for answer in answer_arr if answer[ i ] == element_arr[ 0 ] ]
		answer_arr = new_answer_arr
		if len( answer_arr ) == 1:
			return answer_arr[ 0 ]

	return answer_arr[ 0 ]

if __name__ == '__main__':
	result = solution( [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] )
	print(f'solution( [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] )= { result }, ea = ["ICN", "JFK", "HND", "IAD"], Test = { result ==["ICN", "JFK", "HND", "IAD"] }')
	result = solution( [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] )
	print(f'solution( [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] )= { result }, ea = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"], Test = { result ==["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] }')