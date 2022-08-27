from collections import deque


def solution(queue1, queue2):

	queue_ori_len = len(queue1)
	deque1 = deque( queue1 )
	deque2 = deque( queue2 )
	queue1_sum, queue2_sum = sum(deque1), sum(deque2)
	amount = 0
	for i in range( 3 * queue_ori_len ):
		if queue1_sum == queue2_sum:
			return i

		if queue1_sum > queue2_sum:
			elmt = deque1.popleft()
			queue1_sum -= elmt
			deque2.append( elmt )
			queue2_sum += elmt
		else:
			elmt = deque2.popleft()
			queue2_sum -= elmt
			deque1.append( elmt )
			queue1_sum += elmt
		amount += 1
	return -1


if __name__ == '__main__':
	print( solution( [3, 2, 7, 2], [4, 6, 5, 1] ) )
	print( solution( [1, 2, 1, 2], [1, 10, 1, 2] ) )
	print( solution( [1, 1], [1, 5] ) )

	# list = [ 1, 2, 3, 4 ]
	# a = list.pop( 0 )
	# print(f'{ list = }')
	# print(f'{ a = }')