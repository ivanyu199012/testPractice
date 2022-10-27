def solution(arr):
	answer = []

	prev_element = None
	for num in arr:
		if prev_element is None:
			answer.append( num )
			prev_element = num

		if prev_element != num:
			answer.append( num )
			prev_element = num

	return answer

if __name__ == '__main__':
	print( solution( [1,1,3,3,0,1,1] ) )
	print( solution( [4,4,4,3,3] ) )