#
from collections import deque

def solution( order ):
	result = 0

	if len( order ) == 1:
		return 1

	order_deque = deque( order )
	supp_container = deque()
	yg_deque = deque( range( 1, len( order_deque ) + 1 ) )

	supp_container_item_not_match = False
	for _ in order:
		if len( order_deque ) == 0:
			break

		order_item = order_deque.popleft()

		if len( yg_deque ) == 0:
			supp_container_item = supp_container.pop()
			if order_item == supp_container_item:
				result += 1
				continue
			supp_container_item_not_match = True

		for _ in range( len( yg_deque ) ):
			yg_package = yg_deque.popleft()

			if order_item == yg_package:
				result += 1
				break
			if order_item > yg_package:
				supp_container.append( yg_package )
			if order_item < yg_package:
				yg_deque.appendleft( yg_package )
				supp_container_item = supp_container.pop()
				if order_item == supp_container_item:
					result += 1
					break
				supp_container_item_not_match = True

		if supp_container_item_not_match:
			break

	return result

# def solution( order ):
# 	result = 1

# 	if len( order ) == 1:
# 		return result

# 	order_deque = deque( order )
# 	ori_item = order_deque.popleft()
# 	for _ in range( len( order_deque ) ):
# 		next_item = order_deque.popleft()
# 		if ori_item - next_item == 1:
# 			ori_item = next_item
# 			result += 1
# 			continue

# 		if ori_item - next_item > 1:
# 			break

# 		if ori_item < next_item:
# 			ori_item = next_item
# 			result += 1
# 			continue

# 	return result

if __name__ == '__main__':
	print(f'{ solution( [4, 3, 1, 2, 5] )= }, ea = 2')
	print(f'{ solution( [4, 3, 2, 1, 5] )= }, ea = 5')
	print(f'{ solution( [5, 4, 3, 2, 1] )= }, ea = 5')