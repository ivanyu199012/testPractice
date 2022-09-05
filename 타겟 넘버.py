# BFS
# def solution(numbers, target):
# 	answer = 0
# 	parents = [ 0 ]

# 	for i in range( len( numbers ) ):
# 		leaves = []
# 		for parent in parents:
# 			leaves.append( parent + numbers[ i ] )
# 			leaves.append( parent - numbers[ i ] )
# 		parents = leaves

# 	for leaf in leaves:
# 		if leaf == target:
# 			answer += 1
# 	return answer

# DFS
def solution(numbers, target):
	answer = dfs(numbers, target, 0)
	return answer

def dfs( numbers, target, depth ):
	if depth == len( numbers ):
		return 1 if sum( numbers ) == target else 0
	else:
		answer = 0
		answer += dfs( numbers, target, depth + 1 )
		numbers[ depth ] *= -1
		answer += dfs( numbers, target, depth + 1 )
		return answer

# def gen_coefficient_arr( n ):
# 	coefficient_arr = []

# 	return coefficient_arr

# graph = {
# 	'A': ['B'],
# 	'B': ['A', 'C', 'H'],
# 	'C': ['B', 'D'],
# 	'D': ['C', 'E', 'G'],
# 	'E': ['D', 'F'],
# 	'F': ['E'],
# 	'G': ['D'],
# 	'H': ['B', 'I', 'J', 'M'],
# 	'I': ['H'],
# 	'J': ['H', 'K'],
# 	'K': ['J', 'L'],
# 	'L': ['K'],
# 	'M': ['H']
# }

# def bfs(graph, start_node):
# 	visit = list()
# 	queue = list()

# 	queue.append(start_node)

# 	while queue:
# 		node = queue.pop(0)
# 		if node not in visit:
# 			visit.append(node)
# 			queue.extend(graph[node])

# 		print(f'{ node= }')
# 		print(f'{ visit= }')
# 		print(f'{ queue= }')

# 	return visit

# def dfs(graph, start_node):
# 	visit = list()
# 	stack = list()

# 	stack.append(start_node)

# 	while stack:
# 		node = stack.pop()
# 		if node not in visit:
# 			visit.append(node)
# 			stack.extend(graph[node])

# 		print(f'{ node= }')
# 		print(f'{ visit= }')
# 		print(f'{ stack= }')

# 	return visit

if __name__ == '__main__':
	print(f'{ solution([1, 1, 1, 1, 1], 3)= }')
	print(f'{ solution([4, 1, 2, 1], 4)= }')
	# print(f'{ bfs( graph, "A" )= }')
	# print(f'{ dfs( graph, "A" )= }')
