#
import heapq

def solution( operations ):
	queue = []
	heapq.heapify( queue )

	for operation in operations:
		action, value = operation.split()
		if action == 'I':
			heapq.heappush( queue, int( value ) )
			continue
		if action != 'D':
			continue
		if len( queue ) == 0:
			continue
		if value == '-1':
			heapq.heappop( queue )
			continue
		if value == '1':
			_, queue = get_n_remove_max_element( queue )

	if len( queue ) == 0:
		return [ 0, 0 ]
	if len( queue ) == 1:
		element = heapq.heappop( queue )
		return [ element, element ]
	min_element = heapq.heappop( queue )
	max_element, _ = get_n_remove_max_element( queue )

	return [ max_element, min_element ]

def get_n_remove_max_element( heap ):
	heap = list( map( lambda x: -1 * x,  heap ) )
	heapq.heapify( heap )
	max_element = -1 * heapq.heappop( heap )
	heap = list( map( lambda x: -1 * x,  heap ) )
	heapq.heapify( heap )
	return max_element, heap

if __name__ == '__main__':
	result = solution( ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"] )
	print(f'solution( ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"] )= { result }, ea = [0,0], Test = { result ==[0,0] }')
	result = solution( ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] )
	print(f'solution( ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] )= { result }, ea = [333, -45], Test = { result ==[333, -45] }')