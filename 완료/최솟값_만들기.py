#
def solution( A, B ):
	A.sort()
	B.sort( reverse = True )
	sum = 0
	for i in range( len( A ) ):
		sum += A[i] * B[i]

	return sum
if __name__ == '__main__':
	print(f'{ solution( [1, 4, 2], [5, 4, 4] )= }, ea = 29, Result = { solution( [1, 4, 2], [5, 4, 4] )==29 }')
	print(f'{ solution( [1,2], [3,4] )= }, ea = 10, Result = { solution( [1,2], [3,4] )==10 }')