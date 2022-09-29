#
def solution( grid ):

	result = []
	directions = [ [ -1, 0 ], [ 1, 0 ], [ 0, 1], [ 0, -1 ] ]
	right = { 0: 2, 1: 3, 2: 1, 3: 0 }
	left = { 0: 3, 1: 2, 2: 0, 3: 1 }

	w, h = len( grid ), len( grid[ 0 ] )
	print(f'{ w, h= }')

	cases = [ [  [ 1 ] * 4 for _ in range( w ) ] for _ in range( h ) ]
	for i in range( w ):
		for j in range( h ):
			for k in range( 4 ):

				if cases[ i ][ j ][ k ] == 0:
					continue

				cases[ i ][ j ][ k ] = 0
				count = 0

				tx, ty, td = i, j, k
				while True:

					print(f'before contraction:{ tx, ty, td= }')
					count += 1
					mirror = grid[ i ][ j ]
					if mirror == "R":
						td = right[ td ]
					elif mirror == "L":
						td = left[ td ]

					tx, ty = ( tx + directions[ td ][ 0 ] ) % w, ( ty + directions[ td ][ 1 ] ) % w
					print(f'after contraction:{ tx, ty, td= }')
					if tx == i:
						if ty == j:
							if td == k:
								break

				result.append( count )

	# return result

if __name__ == '__main__':
	print(f'{ solution( ["SL","LR"] )= }, ea = [16]')
	print(f'{ solution( ["S"] )= }, ea = [1,1,1,1]')
	print(f'{ solution( ["R","R"] )= }, ea = [4,4]')