#
from collections import deque

def solution( begin, target, words : list ):

	words.insert( 0, begin )
	word_2_neighors_dict = {}
	for word_i in words:
		word_2_neighors_dict[ word_i ] = []
		for word_j in words:
			if word_i == word_j:
				continue

			if get_word_diff( word_i, word_j ) == 1:
				word_2_neighors_dict[ word_i ].append( word_j )

	visited_set = set()
	not_visited_queue = deque( [ ( begin, 0 ) ] )
	while len( not_visited_queue ) > 0:
		word, count = not_visited_queue.popleft()

		if word == target:
			return count

		if word in visited_set:
			continue
		visited_set.add( word )

		for neighbor in word_2_neighors_dict[ word ]:
			if not neighbor in visited_set:
				not_visited_queue.append( ( neighbor, count + 1 ) )

	return 0

def get_word_diff( word1, word2 ):
	diff_count = 0
	for i in range( len( word1 ) ):
		if word1[ i ] != word2[ i ]:
			diff_count += 1
	return diff_count

if __name__ == '__main__':
	result = solution( "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"] )
	print(f'solution( "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"] )= { result }, ea = 4, Test = { result ==4 }')
	result = solution( "hit", "cog", ["hot", "dot", "dog", "lot", "log"] )
	print(f'solution( "hit", "cog", ["hot", "dot", "dog", "lot", "log"] )= { result }, ea = 0, Test = { result ==0 }')