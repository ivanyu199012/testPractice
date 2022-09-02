# from collections import deque

# def solution(scoville, K):
# 	scoville.sort()
# 	deq_scoville = deque(scoville)
# 	mix_count = 0
# 	while deq_scoville[ 0 ] < K:

# 		if len( deq_scoville ) == 1:
# 			return -1

# 		scoville_amount = deq_scoville.popleft() + 2 * deq_scoville.popleft()

# 		if len( deq_scoville ) > 0:
# 			low = 0
# 			high = len( deq_scoville ) - 1
# 			mid = 0
# 			while low <= high:

# 				mid = (high + low) // 2

# 				# print(f'{ mid= }')
# 				# If x is greater, ignore left half
# 				if deq_scoville[ mid ] < scoville_amount:
# 					low = mid + 1

# 				# If x is smaller, ignore right half
# 				elif deq_scoville[ mid ] > scoville_amount:
# 					high = mid - 1

# 				# means x is present at mid
# 				else:
# 					break

# 			if scoville_amount > deq_scoville[ mid ]:
# 				deq_scoville.insert( mid + 1, scoville_amount )
# 			else:
# 				deq_scoville.insert( mid, scoville_amount )
# 		else:
# 			deq_scoville.insert( 0, scoville_amount )
# 		mix_count += 1

# 	return mix_count

import heapq

def solution(scoville, K):
	heapq.heapify(scoville)
	mix_count = 0
	while scoville[ 0 ] < K:

		if len( scoville ) == 1 and scoville[ 0 ] < K:
			return -1

		heapq.heappush( scoville, heapq.heappop( scoville ) + 2 * heapq.heappop( scoville ) )
		mix_count += 1

	return mix_count

if __name__ == '__main__':
	print(f'{ solution( [1, 3], 8 )= }')
	print(f'{ solution( [1, 2, 3, 9, 10, 12], 7 )= }')
	print(f'{ solution( [1, 2, 3, 9, 10, 12], 12 )= }')
	print(f'{ solution( [1, 2, 3, 9, 10, 12], 1000 )= }')

	# heap = [1, 2, 3, 9, 10, 12]
	# heapq.heapify(heap)
	# print(f'{ heap= }')
	# print(f'{ heap[ 0 ]= }')