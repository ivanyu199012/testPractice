#
from functools import cmp_to_key


def solution( genres, plays ):

	genre_2_view_count_N_plays_dict ={}
	for i in range( len( genres ) ):
		genre = genres[i]
		genre_2_view_count_N_plays_dict[ genre ] = genre_2_view_count_N_plays_dict.get( genre, { "view_count" : 0, "play_indexes" : [] } )
		genre_2_view_count_N_plays_dict[ genre ][ "view_count" ] += plays[ i ]
		genre_2_view_count_N_plays_dict[ genre ][ "play_indexes" ].append( i )

	genre_list = list( genre_2_view_count_N_plays_dict.keys() )
	genre_list.sort( key=lambda genre: genre_2_view_count_N_plays_dict[ genre ][ "view_count" ], reverse=True )

	answer = []
	for genre in genre_list:
		play_indexes : list = genre_2_view_count_N_plays_dict[ genre ][ "play_indexes" ]
		play_indexes.sort( key=lambda play_i : ( -plays[ play_i ], play_i  ) )

		if len( play_indexes ) >= 2:
			answer += play_indexes[ :2 ]
		else:
			answer += [ play_indexes[ 0 ] ]

	return answer

if __name__ == '__main__':
	result = solution( ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500] )
	print(f'solution( ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500] )= { result }, ea = [4, 1, 3, 0], Test = { result ==[4, 1, 3, 0] }')
