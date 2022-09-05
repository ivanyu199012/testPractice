# from collections import deque

# def solution(s):
# 	if len( s ) <= 1:
# 		return 0

# 	front_str_deq = deque( [] )
# 	end_str_deq = deque( s )
# 	while True:

# 		if len( end_str_deq ) < 2:
# 			break

# 		elmt = end_str_deq.popleft()
# 		if elmt == end_str_deq[ 0 ]:
# 			end_str_deq.popleft()
# 			if len( front_str_deq ) > 0:
# 				end_str_deq.appendleft( front_str_deq.pop() )
# 		else:
# 			front_str_deq.append( elmt )

# 	return 1 if ( len( front_str_deq ) + len( end_str_deq ) ) == 0 else 0

def solution( s ):

	stack = []
	for char in s:
		if len( stack ) == 0:
			stack.append( char )
		elif stack[ -1 ] == char:
			stack.pop()
		else:
			stack.append( char )

	return 1 if len( stack ) == 0 else 0

if __name__ == '__main__':
	print(f'{ solution( "baabaa" )= }')
	print(f'{ solution( "cdcd" )= }')

	# s = deque( "baabaa" )
	# elmt = s.popleft()
	# print(f'{ s= }')
	# print(f'{ elmt= }')